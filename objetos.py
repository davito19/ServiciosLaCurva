#!/usr/bin/python3

'''
Design by: Ana Giraldo, Davito
version 1
23/01/2021
'''
#Tabla de codigos
'''
1xy 
2xy not found, command invalid
3xy 
4xy
5xy
'''
#

class Alcohol:
    def __init__(self, id : int, name : str, country : str, unit : int, price : int):
        self.id = id
        self.name = name
        self.country = country
        self.unit = unit
        self.price = price
    def __str__(self):
        return "{};${};disponibles {}, alcohol de {} ".format(self.name, self.price, self.unit, self.country)
    def compra(self, cantidad : int):
        try:
            unit1 = self.unit - cantidad
            if unit1 < 0 :
                return False
            else:
                self.unit -= cantidad
                return True 
        except:
            return None
    def get_id(self):
        return self.id
    def get_country(self):
        return self.country
    def get_name(self):
        return self.name
    def get_stock(self):
        return self.unit
    def get_price(self):
        return self.price
    def set_id(self, id):
        self.id = id
    def set_name(self,name):
        self.name = name
    def set_country(self, country):
        self.country = country
    def set_price(self, price):
        self.price = price

class Cliente:
    def __init__(self,id : str,name : str,account : int, age : int, password : str):
        self.id = id
        self.name = name
        self.account = account
        self.age = age
        self.password = password
    def __str__(self):
        return "{}. {}, edad:{}, cuenta bancaria {}".format(self.id, self.name, self.age, self.account)
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_account(self):
        return self.account
    def get_age(self):
        return self.age
    def set_id(self, id):
        self.id = id
    def set_name(self, name):
        self.name = name
    def set_account(self, account):
        self.account = account
    def set_age(self, age):
        self.age = age
    def set_password(self, control : bool):
        if control:
            print("Se ha enviado un mail ficticio(facil de hacer) de verificación")
            while True:
                new_pass = input("Ingrese la nueva clave")
                new_pass_reply = input("repita la nueva contraseña")
                if new_pass_reply == new_pass:
                    break
            self.password = new_pass
        else:
            print("Ingrese la contraseña o x para cancelar")
            while True:
                password = input("Ingrese la contraseña")
                if password == self.password:
                    new_pass = input('ingrese la nueva contraseña')
                    self.password = new_pass
                    break
                elif password == 'x':
                    break
                else:
                    print("contraseña incorrecta")
    def password_validation(self, password):
        if self.password == password:
            return True
        else:
            return False


class ClienteBanco(Cliente):
    def __init__(self,id : str,name : str,account : int, age : int, password : str, saldo :int, moves : list ):
       super().__init__(id,name, account, age, password)
       self.saldo = saldo
       self.moves = moves
    def set_saldo(self, saldo):
        self.saldo = saldo
    def consignar(self, cantidad):
        self.saldo += cantidad
        self.moves.append("consignacion {};".format(cantidad))
    def retirar(self, cantidad):
        self.saldo -= cantidad
        self.moves.append("retiro de ${}".format(cantidad))
    def get_saldo(self):
        return self.saldo
    def get_moves(self):
        return self.moves

class ClienteAlcoholeria(Cliente):
    def __init__(self,id : str,name : str,account : int, age : int, password : str, moves : list ):
       super().__init__(id,name, account, age, password)
       self.moves = moves


if __name__== '__main__':
    objecto = Alcohol(12, "tequila", "MX", 10, 70000)
    print(objecto)
    print(objecto.compra(7))
    print(objecto.compra(4))
    print(objecto.compra('a'))
    print("--------------------")
    objecto = ClienteBanco("1a", "Ana Giraldo",12345, 21,"12345", 100000, [] )
    print(objecto)
    print(objecto.get_id())
    objecto.set_password(False)