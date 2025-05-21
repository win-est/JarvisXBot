import os
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

def start(update, context):
    user = update.effective_user.first_name
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=(
            f"Привет, {user}!\n\n"
            f"Добро пожаловать в JarvisBot.\n"
            f"Вот твоя ссылка на вход:\n"
            f"https://goo.su/qnkvtL\n"
            f"Промокод: FXX86\n\n"
            f"Не забудь активировать бонус при регистрации!"
        )
    )

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
