import os
from telegram.ext import Updater, CommandHandler

# Bot Token will come from Railway environment variable
TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("🚀 Welcome to TEAM Coin Bot (Symbol: TM)")

def info(update, context):
    update.message.reply_text(
        "🪙 TEAM Coin (TM)\n"
        "A fun meme coin project!\n"
        "More features coming soon..."
    )

def help_cmd(update, context):
    update.message.reply_text(
        "Commands:\n"
        "/start - Welcome message\n"
        "/info - About TEAM Coin\n"
        "/help - Show this menu"
    )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("help", help_cmd))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
