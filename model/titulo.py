import json
import os
import sys
sys.path.append(os.getcwd())
from dbconexion.conexion import DataBaseConexion
class Titulo():
    def __init__(self, id, nombre='Titulo'):
        self.id = id
        self.nombre = nombre
        self.db = DataBaseConexion()

    
    def existe(self):
        self.db.cursor.execute("Select exists(select * from titulo where id="+ str(self.id) + ")" )
        return self.db.cursor.fetchone()[0]

    def getTitulo(self):
        self.db.cursor.execute(f"select nombre from  titulo where id={self.id}")
        return self.db.cursor.fetchone()[0]

    def getAll(self):
        self.db.cursor.execute(f"select titulo.id, titulo.nombre, titulo.precio + rareza.precio, rareza.nombre from titulo inner join rareza on titulo.rarezaid = rareza.id order by id")
        result = self.db.cursor.fetchall()
        return result
    def getPrecio(self):
        self.db.cursor.execute(f"select titulo.precio + rareza.precio from titulo inner join rareza on titulo.rarezaid = rareza.id where titulo.id={self.id}")
        result = self.db.cursor.fetchone()[0]
        return result
    