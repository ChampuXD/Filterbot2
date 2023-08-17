from config import LOG_CHANNEL
from db import *
from asyncio import sleep
from pyrogram import *
from bot import * 

omk = Client.resolve_peer(LOG_CHANNEL)
@Client.on_message(filters.group & filters.new_chat_members)
async def new_group(bot:Client, message):
    bot_id = (await bot.get_me()).id
    member = [u.id for u in message.new_chat_members]        
    if bot_id in member:
       await add_group(group_id=message.chat.id, 
                       group_name=message.chat.title,
                       user_name=message.from_user.username, 
                       user_id=message.from_user.id, 
                       channels=[],
                       f_sub=False,
                       verified=False,plan="")
       m=await message.reply(f"Thanks for adding me in {message.chat.title} ✨")
       num_of_members = await bot.get_chat_members_count(message.chat.id) # get the number of members in the group
       text=f"#NewGroup\n\nGroup: {message.chat.title}\nGroupID: `{message.chat.id}`\nAddedBy: {message.from_user.mention}\nUserID: `{message.from_user.id}`\nNumber of Members: {num_of_members}"
       await bot.send_message(chat_id=omk, text=text)
       await sleep(60)
       await m.delete()