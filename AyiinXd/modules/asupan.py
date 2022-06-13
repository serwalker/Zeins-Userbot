# 🍀 © @tofik_dn
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
# ⚠️ Do not remove credits

from secrets import choice

from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterVoice

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
    if event.chat_id in BLACKLIST_CHAT:
        return await edit_or_reply(
            event, "**Gunakan perintah ini di depan temanmu yang jomblo**"
        )
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        ayang = [
            ayang
            async for ayang in event.client.iter_messages(
                "https://t.me/CeweLogoPack", filter=InputMessagesFilterPhotos
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(ayang), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Gak ada ayang,positif aja mungkin kau jelek haha.**")


@ayiin_cmd(pattern="nc$")
async def _(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await edit_or_reply(
            event, "**Perintah ini Dilarang digunakan di Group ini**"
        )
    xx = await edit_or_reply(event, "`Tunggu Sebentar...`")
    try:
        nc = [
            nc
            async for desah in event.client.iter_messages(
                "@https://t.me/fakyudurov", filter=InputMessagesFilterVideo
            )
        ]
        await event.client.send_file(
            event.chat_id, file=choice(nc), reply_to=event.reply_to_msg_id
        )
        await xx.delete()
    except Exception:
        await xx.edit("**Gak ada video nya tahan sange lu bentar.**")


CMD_HELP.update(
    {
        "asupan": f"**Plugin : **`asupan`\
        \n\n  »  **Perintah :** `{cmd}asupan`\
        \n  »  **Kegunaan : **Untuk Mengirim video asupan secara random.\
        \n\n  »  **Perintah :** `{cmd}ayang`\
        \n  »  **Kegunaan : **Untuk Mengirim foto ayang halu mu haha.\
        \n\n  »  **Perintah :** `{cmd}nc`\
        \n  »  **Kegunaan : **Untuk Mengirim video bokep biar lu coli.\
    "
    }
)
