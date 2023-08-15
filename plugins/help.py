from config import * 
from bot import Client, bot
from pyrogram import *
from pyrogram.types import *
from db import *

HELP_TEXT = f'''To Use me In A Group
First Buy Subscription , Contact the bot owner 👉 @{OWNER}
It Will Cost index Plan Per Month

- Add me in your group & channel with all permissions. 
- Send /verify in group & wait for It To Accept Or Directly Contact To Owner After Request 
- After verification send /index YourChannelID
- Example : /index -100xxxxxxxxxx
- Done ✅. Enjoy 💜❤ )

Remove a Channel with - /remove -100xxxxxxxxxxx
this will help you to remove a indexed channel from your group.

Get connected channels list with - /viewlist '''

PLAN_USD = '''These are the prices in USD:

    `1.2 USD` - per Month 
    `6.2 USD` - per 6 Months
    `12.3 USD` - per Year

    Click on the Buy button to contact the owner'''
    
PLAN_INR = '''**These are the prices in INR:**

    `99 INR` - per Month 
    `599 INR` -  per 6 Months
    `1000 INR` -  per Year

    Click on the `Buy` button to contact the owner'''
BUTTON = InlineKeyboardMarkup([[
  InlineKeyboardButton(text="Buy",callback_data="buy_p"),
  InlineKeyboardButton(text="owner",user_id=OWNER_ID)
  ]])

@Client.on_message(filters.command("help"))
async def help_handler(_, m):
  chat_id = m.chat.id
  await m.reply(HELP_TEXT,reply_markup=BUTTON)
  
@Client.on_callback_query()
async def cb_help(_, q):
  chat_id = q.m.chat.id 
  data = q.data
  BTN = InlineKeyboardMarkup([[
    InlineKeyboardButton("Buy", user_id=OWNER_ID),
    InlineKeyboardButton("USD PRICE", callback_data="usd_p")
    ]])
  BTN_C = InlineKeyboardMarkup([[
    InlineKeyboardButton("Buy", user_id=OWNER_ID),
    InlineKeyboardButton("INR PRICE", callback_data="buy_p")
    ]])
  if data == "buy_p": 
    q.message.edit(PLAN_INR,reply_markup=BTN)
  elif data == "usd_p": 
    q.message.edit(PLAN_USD,reply_markup=BTN_C)