from pyrogram import Client
from secure import api_id, api_hash, proxy_host, proxy_port, proxy_username, proxy_password
from db import engine, Base, Group

app = Client("my_account", api_id=api_id, api_hash=api_hash, proxy=dict(
    hostname=proxy_host,
    port=proxy_port,
    username=proxy_username,
    password=proxy_password
))

groups = []


def create_group(name: str, creator_id: int):
    group = app.create_supergroup(name)
    groups.append({'obj': group, 'owner': creator_id})
    app.add_chat_members(group.id, [creator_id, bot_username])
    app.promote_chat_member(group.id, bot_username, True, True, True, True, True, True, True, True)
    app.promote_chat_member(group.id, creator_id, can_restrict_members=True, can_pin_messages=True,
                            can_promote_members=True)


app.start()

from gendarme_bot_old import bot_username
