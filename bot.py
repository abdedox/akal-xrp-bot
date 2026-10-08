import os
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحبا! بوت AKAL XRP جاهز ✅\n"
        "استخدم /price لمعرفة سعر XRP"
    )

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # جلب سعر XRP من CoinGecko
        url = "https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd"
        r = requests.get(url, timeout=10).json()
        xrp_price = r["ripple"]["usd"]
        await update.message.reply_text(f"💰 سعر XRP الآن: ${xrp_price}")
    except Exception as e:
        await update.message.reply_text(f"حدث خطأ في جلب السعر: {e}")

if __name__ == "__main__":
    if not TOKEN:
        print("خطأ: ضع BOT_TOKEN في متغيرات البيئة")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("price", price))
        print("البوت شغال...")
        app.run_polling()
