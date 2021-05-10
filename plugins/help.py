from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Ingin mendownload video dari youtube??\nSalin link lalu kirim disini"
    await message.reply_text(helptxt)
