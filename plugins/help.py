from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Kirimkan Link Video Youtub Kalian,Pastikan Satu Persatu🌟"
    await message.reply_text(helptxt)
