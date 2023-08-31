import asyncio
from db import *
from config import *
from time import time
from bot import dbot as bot
import time 
from datetime import datetime 
from pyrogram import filters, enums
from pyrogram.types import * 

PLAN = ""
async def check_up(bot):   
  _time = int(time.time()) 
  all_data = await get_all_dlt_data(_time)
  for data in all_data:
    try:
      await bot.delete_messages(chat_id=data["chat_id"],
      message_ids=data["message_id"])           
    except Exception as e:
      err=data
      err["❌ Error"]=str(e)
      print(err)
    await delete_all_dlt_data(_time)



async def check_plan(bot):
  _time = datetime.now().strftime("%Y-%m-%d")
  all_data = await get_plan_data(_time)
  for data in all_data:
    try:
      if _time == data['plan']:
        id = data['_id']
        user = data['user_name']
        await update_group(id, {"verified": False, "plan": ""})
        x = await bot.send_message(chat_id=id, text=f"Subscription Expired ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Buy Now", url=f"t.me/{OWNER}")]]))
        await bot.pin_chat_message(chat_id=id, message_id=x.id)
    except Exception as e:
      await bot.send_message(OWNER_ID, f"Got error in Related Subscription Expired {e}\nUser : {data['user_name']}\nUser ID : {data['user_id']}\nChat ID :{data['_id']}\n")
    
async def run_check_up():
    async with bot: 
        while True:  
           await check_up(bot)
           await check_plan(bot)
           
           
           
           
@bot.on_message(filters.command("buy")) 
async def buy_handle(_, m):
  BUTTON = InlineKeyboardMarkup([[
  InlineKeyboardButton(text="USD PRICE",callback_data="usd_p"),
  InlineKeyboardButton(text="INR PRICE",callback_data="inr_p")
  ]])
  await m.reply(text="All The Available Plans",reply_markup=BUTTON)
  
@bot.on_callback_query()
async def cb_help(_, callback_query: CallbackQuery):
  data = callback_query.data
  PLAN_USD = '''These are the prices in USD:\n\n2 USD - per Month\n6 USD - per 6 Months\n10 USD - per Year\n\nClick on the Buy button to contact the owner'''
  PLAN_INR = '''These are the prices in INR:\n\n100 INR - per Month\n400 INR - per 6 Months\n800 INR - per Year\n\nClick on the Buy button to contact the owner'''
  BTN_1 = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="Buy", url=f"t.me/{OWNER}"),
            InlineKeyboardButton(text="USD PRICE", callback_data="usd_p")
        ]
    ])
  BTN_2 = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="Buy", url=f"t.me/{OWNER}"),
            InlineKeyboardButton(text="INR PRICE", callback_data="inr_p")
        ]
    ])
    
  if data == "inr_p":
    await callback_query.message.edit(PLAN_INR, reply_markup=BTN_1)
  elif data == "usd_p":
    await callback_query.message.edit(PLAN_USD, reply_markup=BTN_2)           
@bot.on_message(filters.command("autodel"))
async def auto_del_handler(_, m):
  chat_id = m.chat.id
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
    
@bot.on_callback_query()
async def cb_autodel(_, callback_query: CallbackQuery):
  id = callback_query.message.chat.id
  user = callback_query.message.from_user.id
  uid = callback_query.from_user.id
  data = callback_query.data
  if uid == user:
    if data == "do_true":
      await update_group(id, {"auto_del": True})
      await callback_query.message.edit("This Chat Auto Delete Message **ON**")
    elif data == "do_false": 
      await update_group(id, {"auto_del": False})
      await callback_query.message.edit("This Chat Auto Delete Message **OFF**")


bot.start()
asyncio.create_task(run_check_up())

