from bot import Client 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

ADMIN = 1791227679

@Client.on_message(filters.command("my") & filters.user(ADMIN))
async def my_handle(_, m):
  BUTTON = [
        [
            InlineKeyboardButton("OWNER", callback_data="okie"),
            InlineKeyboardButton("Coder", callback_data="coder")
        ]
    ]
  await m.reply("Test Button", reply_markup=InlineKeyboardMarkup(BUTTON))

@Client.on_callback_query()
async def cb_me(client: Client, callback_query: CallbackQuery):
    data = callback_query.data
    if data == "okie":
        await callback_query.edit_message_text("Just A Prank")
    elif data == "coder":
        user = await client.get_users(ADMIN)
        await callback_query.answer(f"The coder's username is @{user.username}")
        
