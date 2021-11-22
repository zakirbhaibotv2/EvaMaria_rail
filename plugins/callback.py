from pyrogram import Client, filters
from presets import Presets
from pyrogram.types import CallbackQuery

@Client.on_callback_query(filters.regex(r'^how_btn$'))
async def help_about_button(c: Client, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Presets.HOW_TXT, show_alert=True)
