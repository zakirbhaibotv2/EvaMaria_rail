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
                          reply_markup=[[
            InlineKeyboardButton('Lumber Jack', url='https://tbot.xyz/lumber/#eyJ1Ijo2MTcyNzA3MDIsIm4iOiJULkcgVGFubmhhdXMgIiwiZyI6Ikx1bWJlckphY2siLCJjaSI6IjM5MzY2NzY4MDM4NDk5NDk3OTciLCJpIjoiQlFBQUFHRUZBUUN1emNva3pHMFFmREc2T1NvIn0xM2QxNDI3MWNmMTFjODMxMWMyYWIyNzExZWQ4NGMzO'),
            InlineKeyboardButton('Corasirs', url='https://tbot.xyz/corsairs/#eyJ1Ijo2MTcyNzA3MDIsIm4iOiJULkcgVGFubmhhdXMgIiwiZyI6IkNvcnNhaXJzIiwiY2kiOiIzOTM2Njc2ODAzODQ5OTQ5Nzk3IiwiaSI6IkJRQUFBRjRGQVFDdXpjb2txQkRJU2xXdmF6cyJ9MWY0NzgxYzBjMzJkOTM5OWNkYjRlMjZlZDgxODUyMGU')
            ],[
            InlineKeyboardButton('Music 🎶', url='https://tbot.xyz/math/#eyJ1Ijo2MTcyNzA3MDIsIm4iOiJULkcgVGFubmhhdXMgIiwiZyI6Ik1hdGhCYXR0bGUiLCJjaSI6IjM5MzY2NzY4MDM4NDk5NDk3OTciLCJpIjoiQlFBQUFGY0ZBUUN1emNva3JUWTdMQTgxOTBzIn0yODk2YTk1YzI5ZGVlODg4ZjZjN2Q5ZDQyOTExNGQyZg')
            ],[
            InlineKeyboardButton('🔙 Back', callback_data='start'),
            InlineKeyboardButton('🔒 Close', callback_data='close_data')
                                   ]]
