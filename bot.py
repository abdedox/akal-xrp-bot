import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! AKAL XRP Bot is ready ✅\n"
        "Use /price to get the current XRP price"
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd"
        r = requests.get(url, timeout=10).json()
        xrp_price = r["ripple"]["usd"]
        await update.message.reply_text(f"XRP Price now: ${xrp_price}")
    except Exception as e:
        await update.message.reply_text(f"Error fetching price: {e}")

if __name__ == "__main__":
    if not TOKEN:
        print("Error: BOT_TOKEN not found in environment variables")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("price", price))
        print("Bot is running...")
        app.run_polling(drop_pending_updates=True, close_loop=False)
