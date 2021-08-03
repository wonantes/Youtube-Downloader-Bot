from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Webtoon Group⭐", url="https://t.me/WebtoonOfficialind")],
        [InlineKeyboardButton(
            "Laporkan Masalah", url="https://t.me/aryanvikash")]
    ])
    welcomed = f"Haii <b>{message.from_user.first_name}</b>\n Ketik /Help Untuk Bantuan"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
