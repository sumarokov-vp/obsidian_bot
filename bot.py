import os

from telebot import TeleBot

from credentials import BOT_TOKEN, OBSIDIAN_PATH

bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def welcome(message):
    bot.reply_to(message, "Welcome to the bot!")


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


if __name__ == "__main__":
    bot.infinity_polling()
