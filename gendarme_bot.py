from pyrogram import Client, Filters, InlineKeyboardMarkup, InlineKeyboardButton
import userbot
from secure import api_id, api_hash, proxy_host, proxy_port, proxy_username, proxy_password

app = Client("gendarme", api_id, api_hash, proxy=dict(
    hostname=proxy_host,
    port=proxy_port,
    username=proxy_username,
    password=proxy_password
))


@app.on_message(Filters.command(['start', 'help']))
def start(client, message):
    message.reply_text('Sendu la nomo de via stato')


@app.on_message(Filters.private)
def create_state(client, message):
    message.reply_text(f'Cxu vi reale volas krei staton "{message.text}"?', reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton('Jes, kreu', 'jes')], [InlineKeyboardButton('Ne, nuligu', 'ne')]]))


@app.on_callback_query(Filters.callback_data('jes'))
def confirm(client, callback_query):
    text = callback_query.message.text
    userbot.create_group(text[32:-2], callback_query.from_user.id)


@app.on_callback_query(Filters.callback_data('ne'))
def confirm(client, callback_query):
    pass


app.run()
