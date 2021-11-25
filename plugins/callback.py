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
    await cb.message.edit(InputMediaPhoto("https://telegra.ph/file/8205571d6ac0c64762e47.jpg"), Presets.GAME_TXT, disable_web_page_preview=True,
                          reply_markup=InlineKeyboardMarkup(
            [
                [  # First row
                    InlineKeyboardButton(  # Generates a callback query when pressed
                        "▶ Play - MotoFX 2",
                        url="https://prizes.gamee.com/game-bot/motofx2"
                    ),
                    InlineKeyboardButton(  # Opens a web URL
                        "▶ Play - Little Plane",
                        url="https://prizes.gamee.com/game-bot/5IsYwla"
                    ),
                ],
                [  # Second row
                    InlineKeyboardButton(  # Opens the inline interface
                        "▶ Play - Ride or Die",
                        url="https://prizes.gamee.com/game-bot/rideordie"
                    ),
                    InlineKeyboardButton(  # Opens the inline interface in the current chat
                        "Back",
                        callback_data="start"
                    )
                ]
            ]
        )
    )
