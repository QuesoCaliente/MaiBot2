import os
import sys
sys.path.append(os.getcwd())
from dbconexion.conexion import DataBaseConexion

class Server:
    def __init__(self, nombre='default', prefijo='¡', idserver='1', idchannel='1', limite_twitch=1, idchanneltwitch='1'):
        self.nombre = nombre
        self.prefijo = prefijo
        self.idserver = idserver
        self.idchannel = idchannel
        self.limite_twitch = limite_twitch
        self.idchanneltwitch = idchanneltwitch
        self.db = DataBaseConexion()
    
    def getServer(self):
        self.db.cursor.execute(f"select * from server where idserver='{self.idserver}'")
        server = self.db.cursor.fetchone()
        self.nombre = server[1]
        self.prefijo = server[2]
        self.idserver = server[3]
        self.idchannel = server[4]
        self.limite_twitch = server[5]
        self.idchanneltwitch = server[6]

    def setServer(self):
        if self.existe():
            print('servidor ya existe en la base de datos')
        else:
            self.db.cursor.execute(f"insert into server(nombre, prefijo, idserver) values('{self.nombre}', '{self.prefijo}', '{self.idserver}')")
            self.db.cursor.execute('commit;')

    def updatePrefix(self):
        self.db.cursor.execute(f"update server set prefijo='{self.prefijo}' where idserver='{self.idserver}'")
        self.db.cursor.execute('commit;')

    def updateChannel(self):
        self.db.cursor.execute(f"update server set idchannel='{self.idchannel}' where idserver='{self.idserver}'")
        self.db.cursor.execute('commit;')

    def updateChannelTwitch(self):
        self.db.cursor.execute(f"update server set idchanneltwitch='{self.idchanneltwitch}' where idserver='{self.idserver}'")
        self.db.cursor.execute('commit;')

    def resetChannel(self):
        self.db.cursor.execute(f"update server set idchannel=null where idserver='{self.idserver}'")
        self.db.cursor.execute('commit;')

    def resetChannelTwitch(self):
        self.db.cursor.execute(f"update server set idchanneltwitch=null where idserver='{self.idserver}'")
        self.db.cursor.execute('commit;')

    def existe(self):
        self.db.cursor.execute("Select exists(select * from server where idserver='"+ self.idserver + "')" )
        return self.db.cursor.fetchone()[0]
    
    def existeChannel(self):
        self.db.cursor.execute(f"Select idchannel from server where idserver='{self.idserver}'")
        existecanal = self.db.cursor.fetchone()[0]
        if existecanal == None:
            return False
        return True

    def existeChannelTwitch(self):
        self.db.cursor.execute(f"Select exists(Select idchanneltwitch from server where idserver='{self.idserver}')")
        existecanal = self.db.cursor.fetchone()[0]
        if existecanal == None:
            return False
        return True