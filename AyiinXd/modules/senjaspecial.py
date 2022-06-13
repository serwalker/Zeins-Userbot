# senja-userbot special
# jangan hapus credit memek!


from secrets import choice

from telethon.tl.types import InputMessagesFilterVideo, InputMessagesFilterPhotos

from AyiinXd import BLACKLIST_CHAT
from AyiinXd import CMD_HANDLER as cmd
from AyiinXd import CMD_HELP
from AyiinXd.ayiin import ayiin_cmd, edit_or_reply

@ayiin_cmd(pattern="vl$")
async def _(event):
    try:
        vidlucunya = [
            vidlucu
            async for vidlucu in event.client.iter_messages(
                "@videolucuxauserbot", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(vidlucunya),
            caption=f"Nih kak video lucunya [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video lucu.")



@ayiin_cmd(pattern="vs$")
async def _(event):
    try:
        sadvidnya = [
            sadvid
            async for sadvid in event.client.iter_messages(
                "@sadvideorexa", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(sadvidnya),
            caption=f"Jangan Terlalu Sedih ya kak [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Maaf, kayaknya kamu ga pantes untuk sedih :) .")



@ayiin_cmd(pattern="kpop$")
async def _(event):
    try:
        asupannya = [
            asupan
            async for asupan in event.client.iter_messages(
                "@pictsenadaidol", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(asupannya),
            caption=f"Nih Foto Kpop buat [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan Fotonya coba lagi ya.")


@ayiin_cmd(pattern="ttfyp$")
async def _(event):
    try:
        fypnya = [
            fyp
            async for fyp in event.client.iter_messages(
                "@cah0192837465", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(fypnya),
            caption=f"Tiktok Random Video by [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("Tidak bisa menemukan video, maaf coba lagi.")


@ayiin_cmd(pattern="nc$")
async def _(event):
    try:
        bokepnya = [
            bokep
            async for bokep in event.client.iter_messages(
                "@databasesenja", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(bokepnya),
            caption=f"**negative content by** [{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**tidak ditemukan, tahsn dulu sangenya.**")


@ayiin_cmd(pattern="ppcp$")
async def _(event):
    try:
        ppcpnya = [
            ppcp
            async for ppcp in event.client.iter_messages(
                "@mentahanppcp", filter=InputMessagesFilterPhotos
            )
        ]
        xa = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ppcpnya),
            caption=f"pp couple by [{owner}](tg://user?id={xa.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**tidak ditemukan. **")


@ayiin_cmd(pattern="memeid$")
async def _(event):
    try:
        memexanya = [
            memexa
            async for memexa in event.client.iter_messages(
                "@meme_comic", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(memexanya),
            caption=f"meme by[{owner}](tg://user?id={aing.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**tidak ditemukan. **")


@ayiin_cmd(pattern="ncp$")
async def _(event):
    try:
        kontenrexnya = [
            kontenrex
            async for kontenrex in event.client.iter_messages(
                "@durovbgst", filter=InputMessagesFilterPhotos
            )
        ]
        xa = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(kontenrexnya),
            caption=f"adult photos by [{owner}](tg://user?id={xa.id})",
        )
        await event.delete()
    except Exception:
        await event.edit("**tidak ditemukan. **")


@ayiin_cmd(pattern="lebaran6$")
async def _(event):
    try:
        lebarannya = [
            lebaran
            async for lebaran in event.client.iter_messages(
                "@lebaranxauserbot", filter=InputMessagesFilterPhotos
            )
        ]
        xa = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(lebarannya),
            caption=f"𝐒𝐚𝐲𝐚 [{owner}](tg://user?id={xa.id}) 𝐝𝐚𝐧 𝐬𝐞𝐤𝐞𝐥𝐮𝐚𝐫𝐠𝐚 𝐌𝐞𝐧𝐠𝐮𝐜𝐚𝐩𝐤𝐚𝐧, 𝐌𝐢𝐧𝐚𝐥 𝐀𝐢𝐝𝐳𝐢𝐧 𝐖𝐚𝐥𝐟𝐚𝐢𝐝𝐳𝐢𝐧, 𝐌𝐨𝐡𝐨𝐧 𝐌𝐚𝐚𝐟 𝐋𝐚𝐡𝐢𝐫 𝐃𝐚𝐧 𝐁𝐚𝐭𝐢𝐧",
        )
        await event.delete()
    except Exception:
        await event.edit("**tidak ditemukan. **")


CMD_HELP.update(
    {
        "senjaspecial": f"**Plugin : **senjaspecial\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}vl\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mengirim video lucu secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}vs\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Melihat video sedih secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}kpop\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Melihat foto idol kpop random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}ttfyp\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Melihat video dari tiktok secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}ppcp\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mendapatkan pp couple secara random.\
        \n\n  •  **𝙋𝙚𝙧𝙞𝙣𝙩𝙖𝙝 :** {cmd}memeid\
        \n  ⌬  **𝙁𝙪𝙣𝙜𝙨𝙞 : **Untuk Mendspatkan foto meme secara random.\
"
    }
)
