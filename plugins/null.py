from bot import Client
from db import *
from config import *
from pyrogram import *
from pyrogram.types import *

@Client.on_message(filters.command("my"))
async def my_handle(bot: Client, m: Message):
  BUTTON = [[
    InlineKeyboardButton("OWNER",callback_data="okie"),
    InlineKeyboardButton("Coder",callback_data=1791227679)
    ]]
  await m.reply("Test Button",reply_markup=InlineKeyboardMarkup(BUTTON))
  
@Client.on_callback_query()
async def cb_me(_, q: CallbackQuery): 
  data = q.data
  if data == "okie": 
    await q.message.edit("Just A Prank")
  