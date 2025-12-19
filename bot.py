import os
import random
import requests
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("7694370854:AAHCeRf3HhKd4t6-6CLnLhrSo9-Xjmf1MOw")

keyboard = ReplyKeyboardMarkup(
    [
        ["🪙 Монетка", "🎲 Кубик"],
        ["❓ Так / Ні", "😂 Мем"]
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎲 Бот удачі\n\nОбери дію кнопками 👇",
        reply_markup=keyboard
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🪙 Монетка":
        await update.message.reply_text(
            random.choice(["🪙 Орел", "🪙 Решка"])
        )

    elif text == "🎲 Кубик":
        await update.message.reply_text(
            f"🎲 Тобі випало: {random.randint(1, 6)}"
        )

    elif text == "❓ Так / Ні":
        await update.message.reply_text(
            random.choice(["✅ ТАК", "❌ НІ"])
        )

    elif text == "😂 Мем":
        response = requests.get("https://meme-api.com/gimme").json()
        await update.message.reply_photo(response["url"])

    else:
        await update.message.reply_text(
            "Користуйся кнопками 👇",
            reply_markup=keyboard
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()

