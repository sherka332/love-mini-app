from flask import Flask, send_from_directory
import os
import threading

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

app = Flask(__name__)

MINI_APP_URL = "https://love-mini-app.onrender.com"
BOT_TOKEN = os.environ.get("BOT_TOKEN")


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/api/health")
def health():
    return {
        "status": "ok",
        "message": "Love Mini App API ishlayapti ❤️"
    }


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = InlineKeyboardButton(
        "💖 E'zoza ❤️ Sherbek",
        web_app=WebAppInfo(url=MINI_APP_URL)
    )

    keyboard = InlineKeyboardMarkup([[button]])

    await update.message.reply_text(
        "❤️ Bizning maxsus sahifamiz:",
        reply_markup=keyboard
    )


def run_bot():
    bot = Application.builder().token(BOT_TOKEN).build()
    bot.add_handler(CommandHandler("start", start))
    bot.run_polling()


if __name__ == "__main__":
    if BOT_TOKEN:
        thread = threading.Thread(target=run_bot, daemon=True)
        thread.start()

    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
