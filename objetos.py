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
        return "{}, alcohol de {} costoxunidad de {}".format(self.name, self.country, self.price)
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
