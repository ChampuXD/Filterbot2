from bot import Client
from pyrogram import *
from pyrogram.types import *

ADMIN = 1791227679
@Client.on_message(filters.command("my"))
async def my_handle(bot: Client, m: Message):
  BUTTON = [[
    InlineKeyboardButton("OWNER",callback_data="okie"),
    InlineKeyboardButton("Coder",callback_data=ADMIN)
    ]]
  await m.reply("Test Button",reply_markup=InlineKeyboardMarkup(BUTTON))
  
@Client.on_callback_query()
async def cb_me(_, q: CallbackQuery): 
  data = q.data
  if data == "okie": 
    await q.message.edit("Just A Prank")
  