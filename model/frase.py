import sys, os
import random
sys.path.append(os.getcwd())
from dbconexion.conexion import DataBaseConexion
class Frase():
    def __init__(self, frase='Frase', autor='-Desconocido', anime='Anime', imagen='Url'):
        self.frase = frase
        self.autor = autor
        self.anime = anime
        self.imagen = imagen
        self.db = DataBaseConexion()

    def getRandomQuote(self):
        self.db.cursor.execute("select frase, autor, anime, imagen from frases")
        frases = self.db.cursor.fetchall()
        frase = random.choice(frases)
        self.frase = frase[0]
        self.autor = frase[1]
        self.anime = frase[2]
        self.imagen = frase[3]

