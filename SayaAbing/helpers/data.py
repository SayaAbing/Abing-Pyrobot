from pyrogram.types import InlineKeyboardButton
from SayaAbing import CMD_HELP
class Data:

    text_help_menu = (
        "**Menu Inline Abing-Pyrobot**\n**Prefixes:** ., ?, !, *"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("ᴘᴇɴᴄᴇᴛ ᴀᴊᴀ", callback_data="reopen")]]
