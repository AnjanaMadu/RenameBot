from pyrogram import Client
from pyrogram import idle
from plugins import (
  APP_ID,
  API_HASH,
  TOKEN
)

app = Client(
  'App',
  APP_ID,
  API_HASH,
  bot_token=TOKEN
  plugins=dict(root='plugins')
)

app.start()
print('Bot started!')
idle()
