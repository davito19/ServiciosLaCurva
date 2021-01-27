from socketserver import ThreadingTCPServer, BaseRequestHandler
from base_datos import clientes 

class QueHacer(BaseRequestHandler):
    def handle(self):
        print("conection from {}".format(self.client_address))
        self.bienvenida()
        while True:
                data = self.request.recv(1024).decode()
                if data == '1\r\n':
                    #print("quiere logguearse")
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
            if data == "4\r\n": self.lista()
            if data == "3\r\n": self.retirar()
            if data == "2\r\n": self.consignar()
            if data == "1\r\n": self.consulta()
            #data= (data+"1").encode()
            #self.request.send(data)
        self.request.close()
    def lista(self):
        data = "503. Menu Banco\n"
        data= data.encode()
        self.request.send(data)
        data = "Ingrese 1. para consultar\n"
        data= data.encode()
        self.request.send(data)
        data = "Ingrese 2. para consignar\nIngrese 3. para retirar \nIngrese 4. Para ver el menu\nIngrese bye. para salir\n"
        data= data.encode()
        self.request.send(data)
    def bienvenida(self):
        data = "501. Bienvenido Banco para beber\n"
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
            self.id = data[:-2]
            data = '403. Usuario correcto ingrese contraseña\n'.encode()
            self.request.send(data)
            data = self.request.recv(1024).decode()
            if clientes.search_password(self.id, data[:-2]):
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
    def consulta(self):
        data = ("504. Su saldo es: "+str(clientes.get_saldobanco(self.id))+"\n").encode()
        self.request.send(data)
        self.lista()
    def consignar(self):
        data = "404. Ingrese el saldo a consignar: ".encode()
        self.request.send(data)
        try:
            data = float(self.request.recv(1024).decode())
            clientes.set_saldobanco(self.id , data)
            data = "505. consignación exitosas\n".encode()
            self.request.send(data)
            self.lista()
        except:
            data = "202. Consignacion invalidad\n".encode()
            self.request.send(data)
            self.lista()
    def retirar(self):
        data = "405. Ingrese el saldo a retirar: ".encode()
        self.request.send(data)
        try:
            data = float(self.request.recv(1024).decode())
            boolea = clientes.retire_saldo(self.id, data)
            if boolea:
                data = "506. retiro exitosas\n".encode()
                self.request.send(data)
            else:
                data = "304. Saldo insuficiente\n".encode()
                self.request.send(data)
            self.lista()
        except:
            data = "203. retiro invalidad\n".encode()
            self.request.send(data)
            self.lista()


myserver = ThreadingTCPServer(("localhost", 5569), QueHacer)
myserver.serve_forever()