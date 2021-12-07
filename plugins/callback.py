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
    await cb.message.edit_media(InputMediaPhoto("AgACAgUAAxkBAAO7Ya-FOonsQjO4lJnV5HDxqgWVY18AArauMRs5-XlVIG11Odk_EqQBAAMCAANzAAMjBA"))
                          #reply_markup=InlineKeyboardMarkup([
                           #[InlineKeyboardButton("〽️MAIN CHANNEL 〽️", url="https://t.me/joinchat/Fhcssgw5H8wwMDBl")],
                           #[InlineKeyboardButton("🔰 SERIES", url="https://t.me/netflixorgi")]
                       #]))
                          
