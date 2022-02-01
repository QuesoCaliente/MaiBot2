import json
import os
import random
def cargar_datos(jsonname):
    ruta = 'Mai/data/%s.json' % (jsonname)
    with open(ruta) as contenido:
        results = json.load(contenido)
    return results

def getRandom(lista_quotes):
    quote = random.choice(lista_quotes)
    return quote