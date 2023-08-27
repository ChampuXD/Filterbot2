from bot import Client
from db import *
from config import *
from pyrogram import *
from pyrogram.types import *
from pyrogram.errors import *


@Client.on_message(filters.command("autodel") & filters.group)
async def auto_del_handler(_, m):
  chat_id = m.chat.id
  group = await get_group(chat_id)
  user_id = group['user_id']
  auto_dele = group['auto_del']
  if m.from_user.id == user_id:
    t_text = "This Time Auto-Delete Is **OFF** Click On Button And Set **ON**"
    f_text = "This Time Auto-Delete Is **ON** Click On Button And Set **OFF**"
    
    T_BUTTON = InlineKeyboardMarkup([[
  InlineKeyboardButton("ON",callback_data =f"do_true:{user_id}")
  ]])
    F_BUTTON = InlineKeyboardMarkup([[
  InlineKeyboardButton("OFF",callback_data =f"do_false:{user_id}")
  ]])
    if auto_dele == False:
      await m.reply(t_text,reply_markup=T_BUTTON)
    elif auto_dele == True:
      await m.reply(f_text,reply_markup=F_BUTTON)
    
@Client.on_callback_query()
async def auto_del_cq(_, q):
  id = q.message.chat.id 
  user = q.data.split(":",1)[1]
  uid = q.from_user.id
  data = q.data.split(":",1)[0]
  if uid == user:
    if data == "do_true":
      await update_group(id, {"auto_del": True})
      await q.message.edit("This Chat Auto Delete Message **ON**")
    elif data == "do_false": 
      await update_group(id, {"auto_del": False})
      await q.message.edit("This Chat Auto Delete Message **OFF**")
