from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Grup Chat", url="https://t.me/caritemanh")],
        [InlineKeyboardButton(
            "Developer", url="https://t.me/davialfajr")]
    ])
    welcomed = f"Hallo <b>{message.from_user.first_name}</b>\nGunakan commands /help untuk melanjutkan"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
