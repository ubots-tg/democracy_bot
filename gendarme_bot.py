from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

from secure import TOKEN, request_kwargs


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Привет. Этот бот используется только с @democratic_bot. И вообще он не работает.')


def create_state(update: Update, context: CallbackContext):
    update.message.text

'''
def create_state_step_1(update: Update, context: CallbackContext):
    global state_name_handler
    update.message.reply_text('Как Вы назовёте своё государство?')
    state_name_handler = MessageHandler(Filters.text, create_state_step_2)
    dp.add_handler(state_name_handler)


def create_state_step_2(update: Update, context: CallbackContext):
    global state_name_handler
    dp.remove_handler(state_name_handler)
    keyboard = [[KeyboardButton('Да, создать!'), KeyboardButton('Отмена')]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text(f'Вы уверены, что хотите создать государство **{update.message.text}**?',
                              reply_markup=reply_markup, parse_mode='Markdown')
'''


updater = Updater(token=TOKEN, use_context=True, request_kwargs=request_kwargs)
dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.text, create_state))
updater.start_polling()
