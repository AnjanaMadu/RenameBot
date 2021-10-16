import os
import time
import math
from os.environ import get
from pathlib import Path

AUTH_USER = [1080732057, 1252058587, 1215768187]
APP_ID = int(get('APP_ID', 123456))
API_HASH = get('API_HASH')
TOKEN = get('TOKEN')

def humanbytes(size):
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "K", 2: "M", 3: "G", 4: "T"}
    while size > power:
        size /= power
        raised_to_pow += 1
    final = str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "iB"
    return final

async def progress(current, total, event, start, method):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        msg = "[{0}{1}]\n● **Percent:** {2}%\n".format(
            "".join(["◾️" for i in range(math.floor(percentage / 12.5))]),
            "".join(["▫️" for i in range(8 - math.floor(percentage / 12.5))]),
            round(percentage, 2)
        )
        msg += "● **Status:** {0} of {1}\n● **Speed:** {2}/s".format(
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed)
        )
        await event.edit(f"**{method}**\n{msg}")

async def download_to_local(client, media, update, start):
    path = await client.download_media(
        media,
        progress=progress,
        progress_args=(update, start, "Downloading...")
    )
    return path

async def upload_to_telegram(c, chat, fp, msg, s_time):
    image_ext = tuple([".jpg", ".png", ".jpeg"])
    vid_ext = tuple([".mp4", ".mkv"])
    sticker_ext = tuple([".wepb", ".tgs"])
    song_ext = tuple([".mp3", ".wav", ".m4a"])
    file_name = os.path.basename(fp)
    try:
        if fp.endswith(image_ext):
            await c.send_photo(
                chat,
                fp,
                progress=progress,
                progress_args=(msg, s_time, f"Uploading {file_name}"),
            )
        elif fp.endswith(vid_ext):
            await c.send_video(
                chat,
                fp,
                progress=progress,
                progress_args=(msg, s_time, f"Uploading {file_name}"),
            )
        elif fp.endswith(".gif"):
            await c.send_animation(
                chat,
                fp,
                progress=progress,
                progress_args=(msg, s_time, f"Uploading {file_name}"),
            )
        elif fp.endswith(song_ext):
            await c.send_audio(
                chat,
                fp,
                progress=progress,
                progress_args=(msg, s_time, f"Uploading {file_name}"),
            )
        elif fp.endswith(sticker_ext):
            await c.send_sticker(
                chat,
                fp,
                progress=progress,
                progress_args=(msg, s_time, f"Uploading {file_name}"),
            )
        else:
            await c.send_document(
                chat,
                fp,
                progress=progress,
                progress_args=(msg, s_time, f"Uploading {file_name}"),
            )
    except Exception as e:
        err = str(e)
        return await msg.edit(err)
