from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler

from secure import TOKEN, request_kwargs


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет. Этот бот используется только с @democratic_bot. И вообще он не работает.')


updater = Updater(token=TOKEN, use_context=True, request_kwargs=request_kwargs)
dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))

updater.start_polling()
