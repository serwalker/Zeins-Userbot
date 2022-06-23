# 🍀 © @tofik_dn
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
# ⚠️ Do not remove credits

from secrets import choice

from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterPhotos

from AyiinXd import BLACKLIST_CHAT
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, edit_or_reply


@ayiin_cmd(pattern="asupan$")
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@tedeasupancache", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(asupannya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Tidak bisa menemukan video asupan.**")


@ayiin_cmd(pattern="ayang$")
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        ayangnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@papcecanindo", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(ayangnya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Gak ada ayang?Positif aja mungkin kau jelek haha.**")


@ayiin_cmd(pattern="nc$")
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        ncnya = [
            nc
            async for nc in event.client.iter_messages(
                "@databasesenja", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(ncnya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Gak ada video nya tahan dulu sange lu bentar.**")


@ayiin_cmd(pattern="ncp$")
async def _(event):
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        ncpnya = [
            ncp
            async for ncp in event.client.iter_messages(
                "@durovbgst", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(ncpnya), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Gak ada foto nya tahan dulu sange lu bentar.**")

CMD_HELP.update(
    {
        "senjaspecial": f"**Plugin : **`senjaspecial`\
        \n\n  »  **Perintah :** `{cmd}asupan`\
        \n  »  **Kegunaan : **Untuk Mengirim video asupan secara random.\
        \n\n  »  **Perintah :** `{cmd}ayang`\
        \n  »  **Kegunaan : **Untuk Mengirim foto ayang halu mu haha.\
        \n\n  »  **Perintah :** `{cmd}nc`\
        \n  »  **Kegunaan : **Coba Sendiri Ya Tod.\
        \n\n  »  **Perintah :** `{cmd}ncp`\
        \n  »  **Kegunaan : **Coba Sendiri Ya Tod.\
    "
    }
)
