import time
import os
import pathlib
from pyrogram import Client, filters
from plugins.utils import (
    download_to_local,
    upload_to_telegram,
    delete_file,
    AUTH_USER
)

@Client.on_message(filters.user(AUTH_USER) & filters.text)
async def rename_main(c, m):
    rep = m.reply_to_message
    if not rep:
        return await m.reply('Reply to a message.')
    new_name = m.text
    msg = await m.reply('Downloading to local.')
    start = time.time()
    file_name = await download_to_local(c, rep, msg, start)
    await msg.edit('Renaming...')
    new_name = new_name + pathlib.Path(file_name).suffix
    os.rename(
        src=file_name,
        dst=new_name
    )
    await msg.edit('Uploading to telegram.')
    start = time.time()
    await upload_to_telegram(c, m.chat.id, new_name, msg, start)
    await msg.delete()
    delete_file(file_name)
    delete_file(new_name)

