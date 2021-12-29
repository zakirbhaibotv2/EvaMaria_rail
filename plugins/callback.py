from pyrogram import Client, filters
from presets import Presets
from pyrogram.types import CallbackQuery
from suport.buttons import support_btn
from pyrogram.types import InputMediaPhoto, InputMediaVideo, InputMediaAudio
from pyrogram.types import (
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

Buttonpt = InlineKeyboardMarkup([
                           [InlineKeyboardButton("〽️MAIN CHANNEL 〽️", url="https://t.me/joinchat/Fhcssgw5H8wwMDBl")],
                           [InlineKeyboardButton("🔰 SERIES", url="https://t.me/netflixorgi")]
                       ])


@Client.on_callback_query(filters.regex(r'^how_btn$'))
async def help_about_button(c: Client, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Presets.HOW_TXT, disable_web_page_preview=True,
                          reply_markup=InlineKeyboardMarkup([
                           [InlineKeyboardButton("〽️MAIN CHANNEL 〽️", url="https://t.me/joinchat/Fhcssgw5H8wwMDBl")],
                           [InlineKeyboardButton("🔰 SERIES", url="https://t.me/netflixorgi")]
                       ]))

@Client.on_callback_query(filters.regex(r'^game_btn$'))
async def help_about_button(c: Client, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Presets.GAME_TXT, disable_web_page_preview=True,
                          reply_markup=InlineKeyboardMarkup(
                              [
                               [  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "Lumber Jack",
                        url='https://tbot.xyz/lumber/'
                    ),
                    InlineKeyboardButton(  # Opens a web URL
                        "Corasirs",
                        url="https://tbot.xyz/corsairs/"
                    ),
                ],
                [
                    InlineKeyboardButton(
                         "Math Battle"
                         url='https://tbot.xyz/math/'
                    ),
                ],
                [  # Second row
                    InlineKeyboardButton(  # Opens the inline interface
                        "🔙 Back",
                        callback_data="start"
                    ),
                    InlineKeyboardButton(  # Opens the inline interface in the current chat
                        "🔒 Close",
                        callback_data="Close_data"

                    )
                ]
            ]
        )
    )
