from bot import Client, bot
from db import *
from config import *
from pyrogram import *
from pyrogram.types import *


@Client.on_message(filters.command("start") & filters.private)
async def start_handle(_, m):
  user = m.from_user
  START_MSG = f''' HEY {user.mention} Welcome \n I am Movies Filter Bot\n '''
  BUTTON = InlineKeyboardMarkup([[
    InlineKeyboardButton(text="Help", callback_data="help"),
    InlineKeyboardButton(text="Owner", user_id=OWNER_ID)
  ]])
  await add_user(user_id=user.id)
  await m.reply(START_MSG,reply_markup=BUTTON)

@bot.on_callback_query()
async def cb_help(_, q):
  data = q.data
  if data == "help":
    await q.message.edit("bTa Kya help Chahiye")
