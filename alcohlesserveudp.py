import socket as sk


def udpconexion(cuennta, cantidad):
    string = str(cuennta)+" ; "+ str(cantidad)
    c = sk.socket(sk.AF_INET,sk.SOCK_DGRAM)
    c.sendto(string.encode(),("localhost",6689))
    data, remote = c.recvfrom(1024)
    print(data.decode())
    data, remote = c.recvfrom(1024)
    print(data.decode())
    c.close()
    return data.decode()
