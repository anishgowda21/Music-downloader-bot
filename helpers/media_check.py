from addons.utils import logger

# check if the songs are present in the server


def song_present(filename):
    try:
        music = open(filename, 'rb')
        logger.info(filename+" is preasent in the server")
        return 1
    except FileNotFoundError:
        return None
