import requests
from telegram.utils.helpers import escape_markdown as es
from helpers.caption import caption_maker


def send_media(media_binary, album, title, artist, duration, thumb_binary, msg, update):
    msg.edit_text("Sending the song ⚡️⚡")
    caption = caption_maker(title, album, artist)
    update.message.reply_audio(audio=media_binary, thumb=thumb_binary,
                               title=title, performer=artist, duration=duration, caption=caption, parse_mode="MarkdownV2")
    msg.delete()


def send_song_info(update, album_art_url, song_name, artist):
    caption = f"""*Type : *_{es("Song",version=2)}_\n*Name : *_{es(song_name,version=2)}_\n*Arist : *_{es(artist,version=2)}_"""
    if not album_art_url == "No image":
        cover = requests.get(album_art_url, stream=True).content
    else:
        cover = open("images/botimage.jpg", "rb")
    update.message.reply_photo(
        photo=cover, caption=caption, parse_mode="MarkdownV2")


def send_album_info(update, type, album_art_url, Album_name, count):
    caption = f"""*Type : *_{es(type,version=2)}_\n*Name : *_{es(Album_name,version=2)}_\n*Songs Count : *_{es(str(count),version=2)}_"""
    if not album_art_url == "No image":
        cover = requests.get(album_art_url, stream=True).content
    else:
        cover = open("images/botimage.jpg", "rb")
    update.message.reply_photo(
        photo=cover, caption=caption, parse_mode="MarkdownV2")


def send_status(update, song):
    message = update.message.reply_text(
        f"Downloading 📥\n*{es(song,version=2)}*{es('...',version=2)}", parse_mode="MarkdownV2")
    return message


def wrong_link(update):
    update.message.reply_text(
        "Hey Please send a valid jiosaavn song,album or playlist url ")


def error_msg(update, error):
    msg = f"""*Hey there was an error while processing the media*\n\n{es(error,version=2)}"""
    update.message.reply_text(msg, parse_mode="MarkdownV2")


def process_exist(update):
    update.message.reply_text(
        "Please wait untill previous task is completed 🥺🥺")
