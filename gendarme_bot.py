from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler
import logging
from secure import TOKEN, request_kwargs
import userbot
logging.getLogger("asyncio").setLevel(logging.DEBUG)


def get_full_name_from_user(effective_user):
    return " ".join((effective_user.first_name, effective_user.last_name))


def start(update: Update, context: CallbackContext):
    full_name = get_full_name_from_user(update.message.effective_user)
    logger.info("%s написал start" % full_name)
    update.message.reply_text('Привет! Этот бот используется только с @democratic_bot. И вообще он не работает.')


def creategrp(update: Update, context: CallbackContext):
    attribute = update.message.text.split(' ', 1)[1]
    userbot.create_group(attribute, update.effective_user.id)
    logger.info("%s сделал группу %s" % (get_full_name_from_user(update.message.effective_user), attribute))
    update.message.reply_text('OK')


def setup_logger(level=logging.DEBUG):
    global logger
    logger.name = "system alert"
    fh = logging.FileHandler("log.log")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.setLevel(level)


logger = logging.getLogger("genderame_bot")
setup_logger()
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
bot_username = updater.bot.get_me().username

dp.add_handler(MessageHandler(Filters.text, create_state))
updater.start_polling()
