import twitch
from dbconexion.conexion import DataBaseConexion
class twitch_channel():
    def __init__(self, nombre='nombre', idservidor='1', online=False, mensaje='Mensaje'):
        self.nombre = nombre
        self.idservidor = idservidor
        self.online = online
        self.mensaje = mensaje
        self.db = DataBaseConexion()


    def agregarCanal(self):
        self.db.cursor.execute(f"insert into twitch_channel(nombre, server, online, mensaje) values('{self.nombre}', '{self.idservidor}', False, '{self.mensaje}')")
        self.db.cursor.execute('commit;')

    def eliminarCanal(self):
        self.db.cursor.execute(f"delete from twitch_channel where server='{self.idservidor}' and nombre='{self.nombre}'")

    def getCanal(self):
        self.db.cursor.execute(f"select nombre, server, online, mensaje from twitch_channel where server='{self.idservidor}' and nombre='{self.nombre}'")
        resultado = self.db.cursor.fetchone()
        self.online = resultado[2]
        self.mensaje = resultado [3]

    def updateOnline(self, name, onlain):
        self.db.cursor.execute(f"update twitch_channel set online={onlain} where nombre='{name}'")
        self.db.cursor.execute('commit;')

    def getCanales(self):
        self.db.cursor.execute(f"select nombre, mensaje, online  from twitch_channel where server='{self.idservidor}'")
        canales = self.db.cursor.fetchall()
        return canales

    def existeCanal(self):
        self.db.cursor.execute(f"Select exists(select * from twitch_channel where server = '{self.idservidor}')")
        return self.db.cursor.fetchone()[0]

    def existeCanalTwitch(self):
        self.db.cursor.execute(f"Select exists(select * from twitch_channel where server = '{self.idservidor}' and nombre='{self.nombre}')")
        return self.db.cursor.fetchone()[0]

    def is_limit(self):
        self.db.cursor.execute(f"select nombre from twitch_channel where server = '{self.idservidor}'")
        canales_twitch = len(self.db.cursor.fetchall())
        self.db.cursor.execute(f"select limite_twitch from server where idserver = '{self.idservidor}'")
        limite = self.db.cursor.fetchone()[0]
        if canales_twitch < limite:
            return False
        elif canales_twitch >= limite:
            return True



    