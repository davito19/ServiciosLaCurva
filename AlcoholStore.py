from socketserver import ThreadingTCPServer, BaseRequestHandler
import objetos as ob
import sqlite3 as sql


class BaseDatos:
    def __init__(self, base_datos : str, table : str):
        self.base_datos = base_datos
        self.conexion = sql.connect(self.base_datos)
        self.cursor = self.conexion.cursor()
    def __str__(self):
        return "Base de datos de {}".format(self.base_datos)

class DataCliente(BaseDatos):
    def __init__(self, base_datos : str, table : str):
        super().__init__(base_datos, table)
        self.cursor.execute("SELECT * FROM " + table)
        self.data = self.cursor.fetchall()
        self.clientes = {}
        for i in self.data:
            moves = i[5].split(";")
            self.clientes[i[0]] = ob.ClienteAlcoholeria(i[0],i[1],i[2],i[3],i[4],moves)
    def search_id(self, id):
        for key in self.clientes:
            if id == self.clientes[key].get_id():
                return True
        return False
    def search_password(self, id, password):
        if self.clientes[id].password_validation(password):
            return True
        else:
            return False
    def get_data(self):
        return self.data

clientes =  DataCliente("clientes_licoreria", "Clientes")

class QueHacer(BaseRequestHandler):
    def handle(self):
        print("conection from {}".format(self.client_address))
        self.bienvenida()
        while True:
                data = self.request.recv(1024).decode()
                if data == '1\r\n':
                    print("quiere logguearse")
                    if self.loggueo():
                        break
                    self.lista_loggue()
                elif data == '2\r\n':
                    self.request.close()
                    return None
                else:
                    data = '201. Codigo invalido\n'.encode()
                    self.request.send(data)
        self.lista()
        while True:
            data = self.request.recv(1024).decode()
            if data == "bye\r\n": break
            if data == "3\r\n": self.lista()
            if data == "2\r\n": print("stock")
            if data == "1\r\n": print("comprar")
            #data= (data+"1").encode()
            #self.request.send(data)
        self.request.close()
    def lista(self):
        data = "503. Menu la Curva\n"
        data= data.encode()
        self.request.send(data)
        data = "Ingrese 1. para comprar\n"
        data= data.encode()
        self.request.send(data)
        data = "Ingrese 2. para ver el stock\nIngrese 3. Para ver el menu\nIngrese bye. para salir\n"
        data= data.encode()
        self.request.send(data)
    def bienvenida(self):
        data = "501. Bienvenido a la Curva\n"
        data= data.encode()
        self.request.send(data)
        self.lista_loggue()
    def lista_loggue(self):
        data = "401. Por favor loggueate\n1. Loggueo\n2. Salir\n"
        data= data.encode()
        self.request.send(data)
    def loggueo(self):
        data='402. Ingrese el usuario\n'.encode()
        self.request.send(data)
        data = self.request.recv(1024).decode()
        if clientes.search_id(data[:-2]):
            id = data[:-2]
            data = '403. Usuario correcto ingrese contraseña\n'.encode()
            self.request.send(data)
            data = self.request.recv(1024).decode()
            if clientes.search_password(id, data[:-2]):
                data = '504. Loggueo exitoso\n'.encode()
                self.request.send(data)
                return True
            else:
                data = '303. Clave incorrecta\n'.encode()
                self.request.send(data)
                return False
        else:
            data = '302. Usuario incorrecto\n'.encode()
            self.request.send(data)
            return False



myserver = ThreadingTCPServer(("localhost", 5553), QueHacer)
myserver.serve_forever()

