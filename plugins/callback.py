from bot import Bot
from pyrogram import filters
from presets import Presets
from pyrogram.types import CallbackQuery

@Bot.on_callback_query(filters.regex(r'^about_btn$'))
async def help_about_button(c: Bot, cb: CallbackQuery):
    await cb.answer()
    await cb.message.edit(Presets.HOW_TXT, reply_markup=back_button, disable_web_page_preview=True)
