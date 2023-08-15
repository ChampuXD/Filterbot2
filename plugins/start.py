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
    InlineKeyboardButton(text="Owner", user_id=OWNER_ID),
    InlineKeyboardButton(text="Close", callback_data="close_m")
  ]])
  await add_user(user_id=user.id)
  await m.reply(START_MSG,reply_markup=BUTTON)

@bot.on_callback_query()
async def cb_help(_, q):
  data = q.data
  if data == "close_m":
    await q.message.delete()

@Client.on_message(filters.command("id"))
async def id_handle(_, m):
  chat_id = m.chat.id
  user = m.from_user
  MSG = f"This Chat ID : `{chat_id}`\n"
  
  if m.reply_to_message:
    user_id = m.reply_to_message.from_user.id
    MSG += f"Reply User ID: `{user_id}`"
    await m.reply(MSG)
  else:
    user_id = m.from_user.id
    MSG += f"Your ID: `{user_id}`"
    await m.reply(MSG)

