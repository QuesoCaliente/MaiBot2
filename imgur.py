from imgurpython import ImgurClient
import random

client_id = '3db22def9e42560'
client_secret = '0cfad188f593a07afad9098496930d6a04fdc6cb'

client = ImgurClient(client_id, client_secret)


def getQuotes(album_id):
    listQuotes = []
    items = client.get_album_images(album_id)
    for item in items:
        listQuotes.append(item.link)
    return listQuotes

def getRandomQuote(lista_quotes):
    quote = random.choice(lista_quotes)
    return quote

