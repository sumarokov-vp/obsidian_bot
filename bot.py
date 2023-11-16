# Standard Library
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
        button = InlineKeyboardButton(
            text=os.path.basename(file),
            callback_data=f"open_file${file}",
        )
        keyboard.add(button)
    bot.reply_to(
        message,
        f"Found {len(found_files)} notes for '{query}':",
        reply_markup=keyboard,
    )


@bot.callback_query_handler(func=lambda call: call.data.startswith("open_file$"))
def open_file(call):
    file = call.data.split("$")[1]
    with open(file, "r") as f:
        text = f.read()
    bot.send_message(call.message.chat.id, text)


def grep_files(query) -> List[str]:
    found_files = []

    # Use os.path.join to create the complete path to the Obsidian directory
    obsidian_directory = os.path.join(OBSIDIAN_PATH, "*.md")

    # Use subprocess to run the grep command and capture the output
    try:
        result = subprocess.run(
            ["grep", "-rl", query, obsidian_directory],
            capture_output=True,
            text=True,
            check=True,
        )
        # Split the output into a list of file paths
        found_files = result.stdout.strip().split("\n")
    except subprocess.CalledProcessError as error:
        # Handle errors, e.g., if grep returns a non-zero exit code
        logging.error(error, exc_info=True)
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
    with open(fullpath, "w") as f:
        f.write(text)
    bot.reply_to(message, f"Created note {title}!")


if __name__ == "__main__":
    logging.info("Starting bot...")
    bot.infinity_polling()
