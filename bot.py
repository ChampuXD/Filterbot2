import logging
from datetime import datetime
import asyncio
from config import *
from pyrogram import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

# Initialize logging
FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"
logging.basicConfig(
    handlers=[logging.FileHandler("log.txt"),
              logging.StreamHandler()],
    level=logging.INFO,
    format=FORMAT,
    datefmt="%Y-%m-%d %H:%M:%S",
)
LOGGER = logging.getLogger(__name__)

# Initialize clients
YaaraOP = Client(name="user", session_string=SESSION)
dbot = Client("testbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
class Bot(Client):
    def __init__(self):
        super().__init__(
            "bot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"})

    async def start(self):
        try:
            await super().start()
            await YaaraOP.start()
            await YaaraOP.send_message("me",'chtuiteg')# Start the User client
            LOGGER.info("Bot Started ⚡")
        except Exception as e:
            LOGGER.exception("Error while starting bot: %s", str(e))

    async def stop(self, *args):
        try:
            await super().stop()
            await YaaraOP.stop()  # Stop the User client
            LOGGER.info("Bot Stopped")
        except Exception as e:
            LOGGER.exception("Error while stopping bot: %s", str(e))


@Client.on_message(filters.command("buy")) 
async def buy_handle(Client,m):
  BUTTON = InlineKeyboardMarkup([[
  InlineKeyboardButton(text="USD PRICE",callback_data="usd_p"),
  InlineKeyboardButton(text="INR PRICE",callback_data="inr_p")
  ]])
  await m.reply(text="All The Available Plans",reply_markup=BUTTON)
  
@Client.on_callback_query()
async def cb_help(Client, callback_query: CallbackQuery):
  data = callback_query.data
  PLAN_USD = '''These are the prices in USD:\n\n2 USD - per Month\n6 USD - per 6 Months\n10 USD - per Year\n\nClick on the Buy button to contact the owner'''
  PLAN_INR = '''These are the prices in INR:\n\n150 INR - per Month\n400 INR - per 6 Months\n800 INR - per Year\n\nClick on the Buy button to contact the owner'''
  BTN_1 = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="Buy", url=f"t.me/{OWNER}"),
            InlineKeyboardButton(text="USD PRICE", callback_data="inr_p")
        ]
    ])
  BTN_2 = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="Buy", url=f"t.me/{OWNER}"),
            InlineKeyboardButton(text="INR PRICE", callback_data="usd_p")
        ]
    ])
    
  if data == "inr_p":
    await callback_query.message.edit(PLAN_INR, reply_markup=BTN_1)
  elif data == "usd_p":
    await callback_query.message.edit(PLAN_USD, reply_markup=BTN_2)