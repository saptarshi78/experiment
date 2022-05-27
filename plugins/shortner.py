import os
import aiohttp
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InputTextMessageContent
from pyshorteners import Shortener



LINKLY_API = os.environ.get("LINKLY_API", 558bea95c4cbb568d9c6fc9f2ea86251237aa361)

BUTTONS = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text='⚙ Join Updates Channel ⚙', url='https://telegram.me/HereIsYourLinkShortner')
        ]
    ]
)


@Client.on_message(filters.private & filters.regex(r'https?://[^\s]+'))
async def reply_shortens(bot, update):
    message = await update.reply_text(
        text="`Analysing your link...`",
        disable_web_page_preview=True,
        quote=True
    )
    link = update.matches[0].group(0)
    shorten_urls = await short(link)
    await message.edit_text(
        text=shorten_urls,
        reply_markup=BUTTONS,
        disable_web_page_preview=True
    )


@Client.on_inline_query(filters.regex(r'https?://[^\s]+'))
async def inline_short(bot, update):
    link = update.matches[0].group(0)
    shorten_urls = await short(link)
    answers = [
        InlineQueryResultArticle(
            title="Short Links",
            description=update.query,
            input_message_content=InputTextMessageContent(
                message_text=shorten_urls,
                disable_web_page_preview=True
            ),
            reply_markup=BUTTONS
        )
    ]
    await bot.answer_inline_query(
        inline_query_id=update.id,
        results=answers
    )


async def short(link):
    shorten_urls = "**--Shorted URLs--**\n"
    
    # Linkly.webhostingfree.io shorten
    if LINKLY_API:
        try:
            s = Shortener(api_key=BITLY_API)
            url = s.linkly.short(link)
            shorten_urls += f"\n**link :-** {url}"
        except Exception as error:
            print(f"linkly error :- {error}")
    
   
    
    # Send the text
    try:
        shorten_urls += "\n\nMade by @Saptarshi_78"
        return shorten_urls
    except Exception as error:
        return error
