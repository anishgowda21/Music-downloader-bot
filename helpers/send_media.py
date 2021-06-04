import requests
import traceback
from addons.utils import logger
from helpers.media_check import song_present
from helpers.Downloader import download_song
from helpers.Meta_Adder import add_meta
from helpers.Sender import send_media, send_status, error_msg
dest = "telegramMusic/"


def send(song_data, update):
    try:

        # Get the meta info from the data
        if song_data['song']:
            song_name = song_data['song']
        else:
            song_name = "unknown"

        if song_data['singers']:
            artist = song_data['singers']
        elif song_data['primary_artists']:
            artist = song_data['primary_artists']
        else:
            artist = "unknown artist"

        if song_data['album']:
            album = song_data['album']
        else:
            album = "unknown album"

        if song_data['year']:
            year = song_data['year']
        else:
            year = "unknown year"

        if song_data['lyrics']:
            lyrics = song_data['lyrics'].replace("<br>", "\n")
        else:
            lyrics = None

        if song_data['duration']:
            duration = song_data['duration']
        else:
            duration = 0

        if song_data['image']:
            cover_image = requests.get(song_data['image'], stream=True).content
        else:
            cover_image = open("images/botimage.jpg", "rb")

        if song_data['language']:
            language = song_data['language']
        else:
            language = "Unknown"

        filename = dest+song_name+".mp3"
        msg = send_status(update, song_name)
        # Check if song is present in the server
        if song_present(filename):
            # If the Song is present send the song directly no need to download it agaian
            logger.info(f"Sending {filename}")
            send_media(open(filename, 'rb'), album, song_name, artist, duration,
                       cover_image, msg, update, language)

        else:
            # If the song is not present in the server download the song and convert it
            status = download_song(update, song_data['media_url'], song_name)

            # Check if the song is downloaded correctly
            if status:

                # Add meta data to the song.
                add_meta(filename, album, artist,
                         song_name, year, lyrics, cover_image)

                logger.info(f"Sending {filename}")
                # Send the song
                send_media(open(filename, 'rb'), album, song_name, artist, duration,
                           cover_image, msg, update, language)
            else:
                msg.edit_text("Can't send the song")
    except Exception as e:
        error_msg(update, str(e))
        logger.error(traceback.format_exc())
