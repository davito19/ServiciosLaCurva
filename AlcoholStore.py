from socketserver import ThreadingTCPServer, BaseRequestHandler
import objetos as ob

class QueHacer(BaseRequestHandler):
    def handle(self):
        print("conection from {}".format(self.client_address))
        self.bienvenida()
        while True:
            data = self.request.recv(1024).decode()
            if data == "bye\r\n": break
            if data == "1\r\n": self.lista()
            data= data.encode()
            self.request.send(data)
        self.request.close()
    def lista(self):
        data = "Bienvenido a la Curva\n"
        data= data.encode()
        self.request.send(data)
        data = "Ingrese 1. para comprar\n"
        data= data.encode()
        self.request.send(data)
        data = "Ingrese 2. para ver el stock\n"
        data= data.encode()
        self.request.send(data)
    def bienvenida(self):
        data = "Bienvenido a la Curva\n"
        data= data.encode()
        self.request.send(data)
        data = "Por favor loggueate\n"
        data= data.encode()
        self.request.send(data)


myserver = ThreadingTCPServer(("localhost", 5557), QueHacer)
myserver.serve_forever()
print("hola")