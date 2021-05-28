from telegram.utils.helpers import escape_markdown as es


def caption_maker(title, Album, Singer):
    caption = f"""*Title :* _{es(title,version=2)}_\n*Album :* _{es(Album,version=2)}_\n*Singers :* _{es(Singer,version=2)}_"""
    return caption
