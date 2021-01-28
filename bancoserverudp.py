from socketserver import BaseRequestHandler, ThreadingUDPServer
from base_datos import clientes 
from sys import argv, exit

if len(argv) != 2:
    print("you are idiot")
    exit(1)

class QueHacerUdp(BaseRequestHandler):
    def handle(self):
        #print("Conexion de {}".format(self.client_address))
        data, conn = self.request
        conn.sendto("501\n".encode(),self.client_address)
        data = data.decode().split(";")
        cuenta = int(data[0])-3
        cobro = int(data[1])+3
        user = clientes.obtener_key(cuenta)
        if clientes.retire_saldo(user, cobro):
            conn.sendto("True\n".encode(), self.client_address)
        else:
            conn.sendto("False\n".encode(), self.client_address)
    #def decodificar(self)

ip = str(argv[1])
udp = ThreadingUDPServer((ip, 6689), QueHacerUdp)
udp.serve_forever()