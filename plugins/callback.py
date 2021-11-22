
elif update.data == "confirm_reset":
        await db.delete_user(update.from_user.id)
        await db.add_user(update.from_user.id)
        await update.message.edit_text(
            text="**Settings reset successfully**",
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
