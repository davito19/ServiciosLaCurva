from socketserver import ThreadingTCPServer, BaseRequestHandler
from base_datos import alco
from base_datos import clientesA as clientes

users = 0

class QueHacer(BaseRequestHandler):
    def handle(self):
        global users
        print("conection from {}".format(self.client_address))
        users += 1
        self.bienvenida()
        while True:
                data = self.request.recv(1024).decode()
                if data == '1\r\n':
                    if self.loggueo():
                        break
                    self.lista_loggue()
                elif data == '2\r\n':
                    self.request.close()
                    users -= 1
                    return None
                else:
                    data = '201. Codigo invalido\n'.encode()
                    self.request.send(data)
        self.lista()
        while True:
            data = self.request.recv(1024).decode()
            if data == "bye\r\n": break
            if data == "3\r\n": self.lista()
            if data == "2\r\n": 
                self.stock()
                self.lista()
            if data == "1\r\n": self.comprar()
            else:
                data = '201. Codigo invalido\n'.encode()
                self.request.send(data)
        self.request.close()
        users -= 1
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
                data = '502. Loggueo exitoso\n'.encode()
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
    def stock(self):
        data = ("504. Usuarios conectados: " + str(users) +"\n").encode()
        self.request.send(data)
        data = ("505. \n "+alco.listar_alcoholes()).encode()
        self.request.send(data)

    def comprar(self):
        data = "404. Ingrese el ID del licor a comprar\n".encode()
        self.request.send(data)
        self.stock()
        data =  self.request.recv(1024).decode()
        id = int(data[:-2])
        data = "405. Ingrese la cantidad de botellas \n".encode()
        self.request.send(data)
        data =  self.request.recv(1024).decode()
        cantidad = int(data[:-2])
        if alco.comprar_alcoholes(id, cantidad):
            data = "506. Compra exitosa \n".encode()
            self.request.send(data)
        else:
            data = "304. No hay suficiente inventario disponible \n".encode()
            self.request.send(data)
        self.lista()




myserver = ThreadingTCPServer(("localhost", 5559), QueHacer)
myserver.serve_forever()


