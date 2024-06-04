from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Токен вашего бота
TOKEN = 'token'

def start(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    welcome_message = (f"Hey @{user.username}! It's Blum! 🌟 Your go-to app for crypto trading - all the cool coins and tokens, "
                       "right in your pocket!📱\n\n"
                       "Now we're rolling out our Telegram mini app! Start farming points now, and who knows what cool stuff you'll "
                       "snag with them soon! 🚀\n\n"
                       "Got friends? Bring 'em in! The more, the merrier! 🌱\n\n"
                       "Remember: Blum is where growth thrives and endless opportunities bloom! 🌼")
    
    keyboard = [
        [InlineKeyboardButton("Launch Blum", url="https://t.me/sirdebar_test_bot?startapp=YOUR_APP_HASH")],
        [InlineKeyboardButton("Join Community", url="https://t.me/blumcrypto")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(welcome_message, reply_markup=reply_markup)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()