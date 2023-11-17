# Standard Library
import glob
import logging
import os
import subprocess
import uuid
from typing import List

# Third Party Stuff
import redis
from telebot import TeleBot
from telebot.apihelper import ApiTelegramException
from telebot.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

# My Stuff
from credentials import (
    BOT_TOKEN,
    OBSIDIAN_PATH,
    REDIS_DB,
    REDIS_HOST,
    REDIS_PORT,
)

bot = TeleBot(BOT_TOKEN)
logging.basicConfig(level=logging.INFO)
redis_client = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    db=REDIS_DB,
    decode_responses=True,
    encoding="utf-8",
)


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.reply_to(message, "Welcome to the bot!")


@bot.message_handler(commands=["help"])
def help(message):
    bot.reply_to(
        message,
        "For search just put search string (in one line!)\n"
        "For create note put at least two lines:"
        " first line will be a title, other lines will be a text.\n"
        "Use CMD+Enter to create new line in Telegram.",
    )


@bot.message_handler(commands=["search"])
def search(message):
    message = bot.reply_to(message, "What do you want to search for?")
    bot.register_next_step_handler(message, request_search_query)


# show list of notes with text in them using grep
def request_search_query(message):
    if message.text.startswith("/"):
        return
    query = message.text
    found_files = grep_files(query)
    if len(found_files) == 0:
        bot.reply_to(message, f"No notes found for '{query}'.")
        return
    keyboard = InlineKeyboardMarkup()
    for file in found_files:
        filename = os.path.basename(file)
        logging.debug(filename)
        file_id = str(uuid.uuid4())
        redis_client.set(file_id, file)
        button = InlineKeyboardButton(
            text=filename,
            callback_data=f"open_file${file_id}",
        )
        keyboard.add(button)
    bot.send_message(
        text=f"Search results for '{query}':",
        chat_id=message.chat.id,
        reply_markup=keyboard,
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("open_file$"))
def open_file(call):
    file_id = call.data.split("$")[1]
    filename = str(redis_client.get(file_id))
    filename_without_path = os.path.basename(filename)
    filename_without_extension = filename_without_path.split(".")[0]
    text = f"**{filename_without_extension}**\n\n"
    with open(filename, "r") as f:
        text += f.read()

    text_parts = split_text_with_line_breaks(text=text, max_bytes=3000)
    send_md: bool = len(text_parts) <= 1
    for part in text_parts:
        if send_md:
            md_part = prepare_markdown(part)
        else:
            md_part = None
        send_msg(
            chat_id=call.message.chat.id,
            text=part,
            md_text=md_part,
        )


def split_text(text: str, max_bytes: int) -> List[str]:
    # Split the text into words
    words = text.split()

    # Initialize variables
    current_part = []
    current_length = 0
    parts = []

    for word in words:
        word_bytes = len(word.encode("utf-8"))

        # Check if adding the current word exceeds the maximum length
        if current_length + word_bytes <= max_bytes:
            current_part.append(word)
            current_length += word_bytes
        else:
            # Start a new part
            parts.append(" ".join(current_part))
            current_part = [word]
            current_length = word_bytes

    # Add the last part
    if current_part:
        parts.append(" ".join(current_part))

    return parts


def split_text_with_line_breaks(text, max_bytes):
    # Split the text into lines
    lines = text.splitlines()

    # Initialize variables
    current_part = []
    current_length = 0
    parts = []

    for line in lines:
        line_bytes = len(line.encode("utf-8")) + len("\n".encode("utf-8"))

        # Check if adding the current line exceeds the maximum length
        if current_length + line_bytes <= max_bytes:
            current_part.append(line)
            current_length += line_bytes
        else:
            # Start a new part
            parts.append("\n".join(current_part))
            current_part = [line]
            current_length = line_bytes

    # Add the last part
    if current_part:
        parts.append("\n".join(current_part))

    return parts


def prepare_markdown(text):
    return (
        text.replace("-", "\\-")
        .replace("_", "\\_")
        # .replace("*", "\\*")
        # .replace("`", "\\`")
        .replace(".", "\\.")
        .replace("#", "\\#")
        .replace("(", "\\(")
        .replace(")", "\\)")
        .replace("+", "\\+")
        .replace("!", "\\!")
        .replace(">", "")
        .replace("<", "\\<")
        .replace("{", "\\{")
        .replace("}", "\\}")
        .replace("[", "\\[")
        .replace("]", "\\]")
        .replace("~", "\\~")
        .replace("|", "\\|")
        .replace("=", "\\=")
        .replace("$", "\\$")
    )


def send_msg(chat_id: int, text: str, md_text: str | None = None):
    if md_text:
        try:
            bot.send_message(chat_id, md_text, parse_mode="MarkdownV2")
        except ApiTelegramException as e:
            logging.error(e, exc_info=True)
            logging.info(f"Error sending message: \n{md_text}")
            # try to send without markdown
            try:
                bot.send_message(chat_id, text)
            except ApiTelegramException as e:
                logging.error(e, exc_info=True)
                logging.info(f"Error sending message: \n{text}")
                bot.send_message(chat_id, "Error sending note to Telegram.")
    else:
        try:
            bot.send_message(chat_id, text)
        except ApiTelegramException as e:
            logging.error(e, exc_info=True)
            logging.info(f"Error sending message: \n{text}")
            bot.send_message(chat_id, "Error sending note to Telegram.")


def find_files_by_file_name(directory, part_of_name):
    search_pattern = f"{directory}/*{part_of_name}*.md"
    md_files = glob.glob(search_pattern)
    return md_files


def grep_files(query) -> List[str]:
    obsidian_directory = os.path.join(OBSIDIAN_PATH, "*.md")
    # obsidian_directory = os.path.join("/root/Yandex.Disk/obsidian_wiki/*.md", "*.md")
    # Get a list of file paths that match the pattern
    found_files = find_files_by_file_name(OBSIDIAN_PATH, query)

    file_paths = glob.glob(obsidian_directory)
    # Check if there are any matching files
    if file_paths:
        try:
            # Run the grep command with the list of file paths
            output = subprocess.check_output(
                ["grep", "-rli", query] + file_paths,
                stderr=subprocess.STDOUT,
                text=True,
            )
            found_files += output.strip().split("\n")
        except subprocess.CalledProcessError as e:
            if e.returncode == 1:
                # No matches found
                logging.info(f"No matches found for '{query}'.")
            else:
                logging.error(e, exc_info=True)

    return found_files


@bot.message_handler(func=lambda message: message.text is not None)
def create_note(message):
    lines = message.text.split("\n")
    if len(lines) <= 1:
        request_search_query(message)
        return
    title = lines[0]
    filename = title.replace(" ", "_").replace(".", "_") + ".md"
    fullpath = os.path.join(OBSIDIAN_PATH, filename)
    text = "\n".join(lines[1:])

    # if file exists, append to it
    if os.path.exists(fullpath):
        with open(fullpath, "a") as f:
            f.write("\n")
            f.write(text)
            bot.reply_to(message, f"Appended to note {title}!")
    else:
        with open(fullpath, "w") as f:
            f.write(text)
            bot.reply_to(message, f"Created note {title}!")


if __name__ == "__main__":
    logging.info("Starting bot...")
    bot.infinity_polling()
