from logging import error
import os
from re import A
import requests
from helpers.send_media import send
from helpers.Sender import *
from addons.utils import logger
import traceback
api = os.getenv("API_APP_URL")


def send_song(update, context, query, msg):
    surl = api+"song/?query="+query+"&lyrics=true"
    try:
        context.user_data['downloading'] = True
        data = requests.get(surl)
        if data.status_code == 200 and len(data.json()) > 0:
            data = data.json()
            msg.delete()
            if data['image']:
                image = data['image']
            else:
                image = "No image"
            if data['song']:
                name = data['song']
            else:
                name = "unknown"
            if data['singers']:
                artist = data['singers']
            elif data['primary_artists']:
                artist = data['primary_artists']
            else:
                artist = "unknown artist"
            send_song_info(update, image, name, artist)
            send(data, update)
        else:
            wrong_link(update)
        context.user_data['downloading'] = False
    except Exception as e:
        context.user_data['downloading'] = False
        error_msg(update, str(e))
        logger.error(traceback.format_exc())


def send_album(update, context, query, msg):
    aurl = api+"album/?query="+query+"&lyrics=true"
    try:
        context.user_data['downloading'] = True
        data = requests.get(aurl)
        if data.status_code == 200 and len(data.json()) > 0:
            songs = data.json()['songs']
            if data.json()['image']:
                album_image = data.json()['image']
            else:
                album_image = "No image"
            name = data.json()['name']
            msg.delete()
            send_album_info(update, "Album", album_image, name, len(songs))
            for i, song in enumerate(songs):
                send(song, update)
        else:
            wrong_link(update)
        context.user_data['downloading'] = False
    except Exception as e:
        context.user_data['downloading'] = False
        error_msg(update, str(e))
        logger.error(traceback.format_exc())


def send_playlist(update, context, query, msg):
    purl = api+"playlist/?query="+query+"&lyrics=true"
    try:
        context.user_data['downloading'] = True
        data = requests.get(purl)
        if data.status_code == 200 and len(data.json()) > 0:
            songs = data.json()['songs']
            if data.json()['image']:
                playlist_image = data.json()['image']
            else:
                playlist_image = "No image"
            name = data.json()['listname']
            msg.delete()
            send_album_info(update, "Playlist",
                            playlist_image, name, len(songs))
            for song in data.json()['songs']:
                send(song, update)
        else:
            wrong_link(update)
        context.user_data['downloading'] = False
    except Exception as e:
        context.user_data['downloading'] = False
        error_msg(update, str(e))
        logger.error(traceback.format_exc())
