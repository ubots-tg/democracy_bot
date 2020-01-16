from pyrogram import Client, Filters

from secure import api_id, api_hash, proxy_host, proxy_port, proxy_username, proxy_password

app = Client("my_account", api_id=api_id, api_hash=api_hash, proxy=dict(
    hostname=proxy_host,
    port=proxy_port,
    username=proxy_username,
    password=proxy_password
))


@app.on_message(Filters.private)
def hello(client, message):
    print(1)


groups = []


def create_group(name: str, creator_id: int):
    group = app.create_supergroup(name)
    groups.append({'obj': group, 'owner': creator_id})
    print(group.id)
    print(groups)
    app.add_chat_members(group.id, [creator_id, bot_id])


app.start()

from gendarme_bot import bot_id
