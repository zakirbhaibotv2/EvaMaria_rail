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
                [  
                    InlineKeyboardButton(
                        "Lumber Jack",
                        url="https://tbot.xyz/lumber/"
                    ),
                    InlineKeyboardButton(
                        "Corasirs",
                        url="https://tbot.xyz/corsairs/"
                    ),
                ],
                [
                    InlineKeyboardButton(
                         "Math Battle",
                         url="https://tbot.xyz/math/"
                    ),
                ],
                [  # Second row
                    InlineKeyboardButton(
                        "🔙 Back",
                        callback_data="start"
                    ),
                    InlineKeyboardButton(
                        "🔒 Close",
                        callback_data="close_data"
                    )
                ]
            ]
        )
    )

@Client.on_callback_query(filters.regex(r'^music_btn$'))
async def help_about_button(c: Client, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Presets.MUSIC_TXT, disable_web_page_preview=True,
                          reply_markup=InlineKeyboardMarkup([
                           [InlineKeyboardButton("🔰 SERIES", url="https://t.me/netflixorgi")]
                       ])
