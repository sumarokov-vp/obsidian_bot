# Standard Library
import glob
import logging
import os
import subprocess
from typing import List

# Third Party Stuff
from telebot import TeleBot
from telebot.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

# My Stuff
from credentials import (
    BOT_TOKEN,
    OBSIDIAN_PATH,
)

bot = TeleBot(BOT_TOKEN)
logging.basicConfig(level=logging.INFO)


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.reply_to(message, "Welcome to the bot!")


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
        button = InlineKeyboardButton(
            text=filename,
            callback_data=f"open_file${filename}",
        )
        keyboard.add(button)
    bot.reply_to(
        message,
        f"Found {len(found_files)} notes for '{query}':",
        reply_markup=keyboard,
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("open_file$"))
def open_file(call):
    filename = call.data.split("$")[1]
    message_text = f"*{filename}*\n\n"
    fullpath = os.path.join(OBSIDIAN_PATH, filename)
    with open(fullpath, "r") as f:
        text = f.read()
    message_text += (
        text.replace("-", "\\-")
        .replace("_", "\\_")
        .replace("*", "\\*")
        # .replace("`", "\\`")
        .replace(".", "\\.")
        .replace("#", "\\#")
        .replace("(", "\\(")
        .replace(")", "\\)")
        .replace("+", "\\+")
        .replace("!", "\\!")
        .replace(">", "\\>")
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

    bot.send_message(call.message.chat.id, message_text, parse_mode="MarkdownV2")


def grep_files(query) -> List[str]:
    obsidian_directory = os.path.join(OBSIDIAN_PATH, "*.md")
    # obsidian_directory = os.path.join("/root/Yandex.Disk/obsidian_wiki/*.md", "*.md")
    # Get a list of file paths that match the pattern
    file_paths = glob.glob(obsidian_directory)
    found_files = []

    # Check if there are any matching files
    if file_paths:
        try:
            # Run the grep command with the list of file paths
            output = subprocess.check_output(
                ["grep", "-rl", query] + file_paths,
                stderr=subprocess.STDOUT,
                text=True,
            )
            found_files = output.strip().split("\n")
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
