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
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@Database_TonicUbot", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"Nih kak asupannya [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video asupan.")



@ayiin_cmd(pattern="desah$")
async def _(event):
    try:
        desahnya = [
            desah
            async for desah in event.client.iter_messages(
                "@Desahan_Enak", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(desahnya),
            caption=f"Nih kak desahannya [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan desahan.")


        
@ayiin_cmd(pattern="ayang$")
async def _(event):
    try:
        ayangnya = [
            ayang
            async for ayang in event.client.iter_messages(
                "@papcecanindo", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ayangnya),
            caption=f"Nih Ayang Aku 😘 [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Gada Yang Mau Sama Kamu Karena Kamu ga Gud Luking🤪.")

CMD_HELP.update(
    {
        "asupan": f"**➢ Plugin : **asupan\
        \n\n ┌✪ **Syntax :** {cmd}asupan\
        \n └✪ **Function : **Untuk Mengirim video asupan secara random.\
        \n\n ┌✪ **Syntax :** {cmd}ayang\
        \n └✪ **Function : **Untuk Mencari Ayang.\
        \n\n ┌✪ **Syntax :** {cmd}desah\
        \n └✪ **Function : **Untuk Mengirim voice desah secara random.\
    "
    }
)
