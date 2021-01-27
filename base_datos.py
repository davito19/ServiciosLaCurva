import sqlite3 as sql
import objetos as ob

class BaseDatos:
    def __init__(self, base_datos : str, table : str):
        self.base_datos = base_datos
        self.conexion = sql.connect(self.base_datos, check_same_thread=False)
        self.cursor = self.conexion.cursor()
        self.table = table
    def __str__(self):
        return "Base de datos de {}".format(self.base_datos)

class DataCliente(BaseDatos):
    def __init__(self, base_datos : str, table : str):
        super().__init__(base_datos, table)
        self.cursor.execute("SELECT * FROM " + self.table)
        self.data = self.cursor.fetchall()
        self.clientes = {}
        for i in self.data:
            moves = i[6].split(";")
            self.clientes[i[0]] = ob.ClienteBanco(i[0],i[1],i[2],i[3],i[4],i[5],moves)
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
    def get_saldobanco(self,id):
        self.refres2(id)
        return self.clientes[id].get_saldo()
    def set_saldobanco(self, id, cantidad):
        self.refres2(id)
        self.clientes[id].consignar(cantidad)
        self.refresh(id)
    def retire_saldo(self, id, cantidad):
        if self.get_saldobanco(id) >= cantidad:
            self.clientes[id].retirar(cantidad)
            self.refresh(id)
            return True
        else:
            return False
    def refresh(self, id):
        sq = "UPDATE Clientes SET Saldo = '"+str(self.clientes[id].get_saldo())+ "' where ID = '" + id +"'"
        self.cursor.execute(sq)
        self.conexion.commit()
    def refres2(self, id):
        self.cursor.execute("SELECT * FROM " + self.table)
        self.data = self.cursor.fetchall()
        self.clientes = {}
        for i in self.data:
            moves = i[6].split(";")
            self.clientes[i[0]] = ob.ClienteBanco(i[0],i[1],i[2],i[3],i[4],i[5],moves)
        
    def obtener_key(self,cuenta):
        for i in self.clientes:
            if self.clientes[i].get_account() == cuenta:
                return i
        return None

class DataClienteA(BaseDatos):
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

class DataAlcohol(BaseDatos):
    def __init__(self, base_datos : str, table : str):
        super().__init__(base_datos, table)
        self.cursor.execute("SELECT * FROM " + table)
        self.data = self.cursor.fetchall()
        self.alcoholes = {}
        for i in self.data:
            self.alcoholes[i[0]] = ob.Alcohol(i[0], i[1], i[2], i[3], i[4])
    def listar_alcoholes(self):
        string = ""
        for key in self.alcoholes:
            string += str(self.alcoholes[key])
        return string
    def comprar_alcoholes(self, id, cantidad):
        temp = self.alcoholes[id].compra(cantidad)
        self.refresh(id)
        return temp
    def refresh(self, id):
        sql = "UPDATE ALCOHOLES SET Unidades = '"+str(self.alcoholes[id].get_stock())+ "' where ID = '" + str(id) +"'"
        self.cursor.execute(sql)
        self.conexion.commit()
    def refres2(self,id):
        self.cursor.execute("SELECT * FROM " + table)
        self.data = self.cursor.fetchall()
        self.alcoholes = {}
        for i in self.data:
            self.alcoholes[i[0]] = ob.Alcohol(i[0], i[1], i[2], i[3], i[4])
    

clientesA =  DataClienteA("clientes_licoreria", "Clientes")
alco = DataAlcohol("Alcoholes", "ALCOHOLES")
clientes =  DataCliente("clientes_banco", "Clientes")