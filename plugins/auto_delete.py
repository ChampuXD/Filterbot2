from bot import Client
from db import *
from config import *
from pyrogram import *
from pyrogram.types import *
from pyrogram.errors import *


@Client.on_message(filters.command("autodel"))
async def auto_del_handler(bot: Client, m):
  chat_id = m.chat.id
  if m.text == "/autodel":
    return None
  if m.chat.type == enums.ChatType.PRIVATE:
    return await m.reply("Please Use In Group Chat")
  group = await get_group(chat_id)
  user_id = group['user_id']
  auto_dele = group['auto_del']
  if m.from_user.id == user_id:
    t_text = "This Time Auto-Delete Is **OFF** Click On Button And Set **ON**"
    f_text = "This Time Auto-Delete Is **ON** Click Off Button And Set **OFF**"
    
    T_BUTTON = InlineKeyboardMarkup([[
  InlineKeyboardButton("ON",callback_data ="do_true")
  ]])
    F_BUTTON = InlineKeyboardMarkup([[
  InlineKeyboardButton("OFF",callback_data ="do_false")
  ]])
    if auto_dele == False:
      await m.reply(t_text,reply_markup=T_BUTTON)
    elif auto_dele == True:
      await m.reply(f_text,reply_markup=F_BUTTON)
    
@Client.on_callback_query()
async def auto_del_cq(bot:Client, q:CallbackQuery):
  id = q.message.chat.id
  user = q.message.from_user.id
  uid = q.from_user.id
  data = q.data
  if uid == user:
    if data == "do_true":
      await update_group(id, {"auto_del": True})
      await q.message.edit("This Chat Auto Delete Message **ON**")
    elif data == "do_false": 
      await update_group(id, {"auto_del": False})
      await q.message.edit("This Chat Auto Delete Message **OFF**")
