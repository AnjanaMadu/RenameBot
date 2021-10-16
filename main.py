import logging
from pyrogram import Client
from pyrogram import idle
from plugins.utils import (
  APP_ID,
  API_HASH,
  TOKEN
)

logging.basicConfig(
  level=logging.INFO,
  format="%(asctime)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)

app = Client(
  'App',
  APP_ID,
  API_HASH,
  bot_token=TOKEN,
  plugins=dict(root='plugins')
)

app.start()
LOGGER.info('Bot started!')
idle()
