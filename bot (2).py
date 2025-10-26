import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = os.getenv("BOT_TOKEN")  # ← يأخذ التوكن من إعدادات السيرفر

async def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🎮 افتح سين جيم العراق", web_app={"url": "https://siudurtsche-rgb.github.io/seenjeemiraq/"})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("🎯 أهلاً بك في *سين جيم العراق* — اضغط الزر أدناه لتبدأ:", reply_markup=reply_markup)

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()