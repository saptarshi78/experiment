from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_TEXT = """Hello {} 😌
I am an official link shortner telegram bot for HereIsYourLink Shortner.

>> `I can short any type of link`

Made by @Saptarshi_78"""

START_BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton('⚙ Join Updates Channel ⚙', url='https://telegram.me/HereIsYourLinkShortner')
        ]
    ]
)

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        reply_markup=START_BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
