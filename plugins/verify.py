from config import *
from db import *
from pyrogram import *
from pyrogram.types import *

@Client.on_message(filters.group & filters.command("auth"))
async def _verify(bot: Client, message):
    try:
        group = await get_group(message.chat.id)
        user_id = group["user_id"]
        user_name = group["user_name"]
        verified = group["verified"]
    except:
        return await bot.leave_chat(message.chat.id)

    try:
        user = await bot.get_users(user_id)
    except:
        return await message.reply(f"❌ {user_name} Need to start me in PM!")

    if message.from_user.id != user_id:
        return await message.reply(f"Only {user.mention} can use this command 😁")

    if verified:
        return await message.reply("You are already authentic Person")

    try:
        link = (await bot.get_chat(message.chat.id)).invite_link
    except:
        return message.reply("❌ Make me admin here with all permissions!! except anonymous ")

    members_count = await bot.get_chat_members_count(chat_id=message.chat.id)

    text = f"#NewRequest\n\n"
    text += f"Requested By: {message.from_user.mention}\n"
    text += f"User ID: `{message.from_user.id}`\n"
    text += f"Group: [{message.chat.title}]({link})\n"
    text += f"Group ID: `{message.chat.id}`\n"
    text += f"Total Members: `{members_count}`\n"

    keyboard = [[InlineKeyboardButton("✅ Approve", callback_data=f"verify:approve:{message.chat.id}"),
                 InlineKeyboardButton("❌ Decline", callback_data=f"verify:decline:{message.chat.id}")],
                [InlineKeyboardButton("👀 View Group", url=f"{link}")]]

    await bot.send_message(chat_id=LOG_CHANNEL, text=text, disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(keyboard))
    await message.reply("authentication request sent ✅\nWe will notify you personally when it is approved.")

@Client.on_callback_query(filters.regex(r"^verify"))
async def verify_(bot, update):
    id = int(update.data.split(":")[2])
    group = await get_group(id)
    name  = group["name"]
    user  = group["user_id"]
    if update.data.split(":")[1]=="approve":
       await update_group(id, {"verified":True})
       await bot.send_message(chat_id=user, text=f"Your authentication request for {name} has been approved ✅")
       await update.message.edit(update.message.text.replace("#NewRequest", "#Approved"))
    else:
       await delete_group(id)
       await bot.send_message(chat_id=user, text=f"Your authentication request for {name} has been declined Becauss You Dont Bought Paid /buy Now")
       await update.message.edit(update.message.text.replace("#NewRequest", "#Declined"))