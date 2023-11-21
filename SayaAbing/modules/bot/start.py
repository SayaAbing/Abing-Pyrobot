# if you can read this, this meant you use code from Geez | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez | Ram Team
import random
from SayaAbing import app
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from config import OWNER_ID as owner 

@app.on_callback_query()
def pmowner(client, callback_query):
    user_id = owner
    message = "Lu Siapa Anjeng!!!!"
    client.send_message(user_id, message)
    client.answer_callback_query(callback_query.id, text="Message sent")

logoabing = [
    "https://telegra.ph//file/90d5d3542f4f208c8b9fa.jpg",
    "https://telegra.ph//file/56686deccbe0441927998.jpg",
    "https://telegra.ph//file/56686deccbe0441927998.jpg",
    "https://telegra.ph//file/90d5d3542f4f208c8b9fa.jpg"
]

alive_logo = random.choice(logoabing)

@app.on_message(filters.command("start") & filters.private)
async def start(app, message):
    chat_id = message.chat.id
    file_id = alive_logo
    caption = "Hi, Saya Asisstant Abing-Pyrobot\nTidak Ada Yang Special Kecuali Indomie."
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Support", url="https://t.me/ab1ngsupport"),
            InlineKeyboardButton("Channel", url="https://t.me/ab1ngstore"),
        ],
    ])

    await app.send_photo(chat_id, file_id, caption=caption, reply_markup=reply_markup)
