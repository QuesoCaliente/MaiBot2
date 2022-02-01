from bs4 import BeautifulSoup
import requests
import urllib.parse
def getKonaImage(anime_name):
    lista_imagenes = []
    contador = 0
    imagenkonachan = ''
    anime_name = anime_name.replace(' ', '_')
    print(anime_name)
    url = 'https://konachan.com/post?tags={}%20rating:safe'.format(anime_name)
    animerequest = requests.get(url)
    print(animerequest.url)
    if animerequest.status_code == 200:
        print('entro en el 200')
        html = BeautifulSoup(animerequest.text, "html.parser")
        if html.find('ul', {'id':'post-list-posts'}) is not None:
            konacontainer = html.find('ul', {'id':'post-list-posts'}).find_all('li')
            for konaimage in konacontainer:
                imagen = ''
                if konaimage.find('a', {'class':'directlink'}) is not None:
                    imagen = konaimage.find('a', {'class':'directlink'}).get('href')
                    contador+=1
                    lista_imagenes.append(imagen)
        else:
            lista_imagenes.append('https://i.imgur.com/UyZ8YzS.jpg')
    return lista_imagenes