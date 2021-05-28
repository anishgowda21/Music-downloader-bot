from logging import log
from mutagen.id3 import ID3, APIC, _util, USLT
from mutagen.mp3 import EasyMP3
from mutagen.easyid3 import EasyID3
from addons.utils import logger
EasyID3.RegisterTextKey("year", "TDRC")


def add_meta(filename, album, artist, title, year, lyrics, cover_image):

    # Add Album art
    try:
        audio = EasyMP3(filename, ID3=ID3)
        try:
            audio.add_tags()
        except _util.error:
            pass
        audio.tags.add(APIC(encoding=3, mime='image/jpeg',
                       type=3, desc='Cover(front)', data=cover_image))
        audio.save()
        logger.info("Added Album art")
    except Exception as e:
        logger.error(e)
        pass

    # Add Album name, Artist name,year,Title and lyrics
    try:
        tags = EasyMP3(filename)
        if album:
            tags['album'] = album
            logger.info("Added Album")
        if artist:
            tags['artist'] = artist
            logger.info("Added Artist")
        if title:
            tags['title'] = title
            logger.info("Added Title")
        if year:
            tags['year'] = year
            logger.info("Added Year")
        tags.save()

        if lyrics:
            tags = ID3(filename)
            uslt_output = USLT(encoding=3, lang=u'eng',
                               desc=u'desc', text=lyrics)
            tags["USLT::'eng'"] = uslt_output
            logger.info("added Lyrics\n")

            tags.save()

    except Exception as e:
        logger.error(e)
        pass
