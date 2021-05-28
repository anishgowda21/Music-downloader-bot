import youtube_dl
from addons.utils import logger
from helpers.Sender import error_msg

# Download the song and convert it to mp3


def download_song(update, url, name):

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"telegramMusic/{name}"+".%(ext)s",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320"
        }]
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download((url,))
            logger.info(f"Downloaded and converted {name}")
            return 1
    except Exception as e:
        logger.error(e)
        error_msg(update, str(e))
        return 0
