from socketserver import ThreadingTCPServer, BaseRequestHandler
import objetos as ob

cliente = ob.ClienteAlcoholeria("a1","Ana",12345,21,"ana",[])

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
        if data[:-2] == cliente.get_id():
            data = '403. Usuario correcto ingrese contraseña\n'.encode()
            self.request.send(data)
            data = self.request.recv(1024).decode()
            if cliente.password_validation(data[:-2]):
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


myserver = ThreadingTCPServer(("localhost", 5559), QueHacer)
myserver.serve_forever()
print("hola")