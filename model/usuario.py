import json
import os
import sys
sys.path.append(os.getcwd())
from dbconexion.conexion import DataBaseConexion
class Usuario:

    def __init__(self, idusuario='0', nombre='username', banner_url='https://i.imgur.com/6z4FbhE.jpg', titulo_id=1, biografia='Sin Descripcion', maicoins=1, maicoins_img=1):
        self.idusuario = idusuario
        self.nombre = nombre
        self.banner_url = banner_url
        self.titulo_id = titulo_id
        self.biografia = biografia
        self.maicoins = maicoins
        self.maicoins_img = maicoins_img
        self.db = DataBaseConexion()
    
    def getUsuario(self):
        self.db.cursor.execute("select * from usuarios where idusuario='"+ self.idusuario + "'")
        user = self.db.cursor.fetchone()
        self.nombre = user[1]
        self.banner_url = user[2]
        self.titulo_id = user[3]
        self.biografia = user[4]
        self.maicoins = user[5]
        self.maicoins_img = user[6]

    def setUsuario(self):
        self.db.cursor.execute(f"insert into usuarios(idusuario ,nombre, banner_url, titulo_id, biografia, maicoins, maicoins_img_id) values('{self.idusuario}','{self.nombre}', '{self.banner_url}', {self.titulo_id}, '{self.biografia}', {self.maicoins}, {self.maicoins_img})")
        self.db.cursor.execute('commit;')

    def updateBiografia(self):
        self.db.cursor.execute(f"update usuarios set biografia = '{self.biografia}' where idusuario = '{self.idusuario}'")

    def updateBanner(self):
        self.db.cursor.execute(f"update usuarios set banner_url = '{self.banner_url}' where idusuario = '{self.idusuario}'")

    def updateTitulo(self):
        self.db.cursor.execute(f"update usuarios set titulo_id = {self.titulo_id} where idusuario = '{self.idusuario}'")
        


    def getTitulo(self):
        self.db.cursor.execute("select nombre from titulo where id=" + str(self.titulo_id))
        titulo = self.db.cursor.fetchone()[0]
        return titulo



    def getTitulos(self):
        self.db.cursor.execute(f"select titulo.id, titulo.nombre, rareza.nombre  from usuarios_titulos inner join usuarios on usuarios.idusuario = usuarios_titulos.usuarioid inner join titulo on usuarios_titulos.tituloid = titulo.id inner join rareza on titulo.rarezaid = rareza.id where usuarios.idusuario = '{self.idusuario}'")
        result = self.db.cursor.fetchall()
        print(result)
        return result

    #def getServer(self):
        #self.db.cursor.execute("select idserver from server where id=" + str(self.server))
        #server = self.db.cursor.fetchone()[0]
        #return server


    def updateMaiCoins(self):
        self.db.cursor.execute(f"update usuarios set maicoins={self.maicoins} where idusuario ='{self.idusuario}'")
    def getMaiCoins_img(self):
        self.db.cursor.execute("select url from maicoins_img where id="+ str(self.maicoins_img))
        maicoins_img = self.db.cursor.fetchone()[0]
        return maicoins_img
    
    def existe(self):
        self.db.cursor.execute("Select exists(select * from usuarios where idusuario='"+ self.idusuario + "')" )
        return self.db.cursor.fetchone()[0]


    def existePerfilTitulos(self):
        self.db.cursor.execute("Select exists(select * from usuarios_titulos where usuarioid='"+ self.idusuario + "')" )
        return self.db.cursor.fetchone()[0]

    def existeTituloPerfil(self, id):
        self.db.cursor.execute("Select exists(select * from usuarios_titulos where tituloid='"+ str(id) + "' and usuarioid='"+ self.idusuario +  "')" )
        return self.db.cursor.fetchone()[0]

    def setTituloDefault(self):
        self.db.cursor.execute(f"Insert into usuarios_titulos(tituloid, usuarioid) values(1, '{self.idusuario}')")

    def setTituloPerfil(self):
        self.db.cursor.execute(f"Insert into usuarios_titulos(tituloid, usuarioid) values({self.titulo_id}, '{self.idusuario}')")