from pyrogram import Client, filters
from presets import Presets
from pyrogram.types import CallbackQuery
from suport.buttons import support_btn

@Client.on_callback_query(filters.regex(r'^how_btn$'))
async def help_about_button(c: Client, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Presets.HOW_TXT, reply_markup=support_btn, disable_web_page_preview=True)
