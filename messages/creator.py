from telegram.utils.helpers import escape_markdown as es


def start_msg(name):
    msg = f"""*Hey {es(name,version=2)}* โโ *welcome to Jiosaavn downloader bot* โกโก\n
    _Just send me a jiosaavn song or album link I will send you the audio_\n
made by @phantom2152 ๐๐"""
    return msg


def help_msg():
    help = """โน๏ธโโ *help*\n
*just send me a jiosaavn song,album or playlist link, I will send you the audio with lyrics*โกโก"""
    return help
