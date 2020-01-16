import logging
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler

from secure import TOKEN, request_kwargs
import userbot


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
updater = Updater(token=TOKEN, use_context=True, request_kwargs=request_kwargs)
dp = updater.dispatcher
dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('creategrp', creategrp))

bot_id = updater.bot.get_me().id

updater.start_polling()
