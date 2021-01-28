# ServiciosLaCurva

# Operacion

## Servidor licorera

Atiende conexiones tcp por el puerto 5559, permite ingresar con usuario y contraseña, comprar y revisar el stock de alcoholes.
permite conexion UDP cifrada con el banco para realizar pagos.

## Servidor Banco

Atiende conexiones TCP de clientes por el puerto 5569, permite ingresar con usuario y contraseña,, consultar, consignar y retirar su dinero.
Ademas atiende conexiones UDP cifradas por el puerto 6689 para realizar pagos de compras.

# Ejecucion

corra el programa pro.py utilizando el comando en consola:
>> python3 pro.py

Asegurese de estar parado sobre la carpeta donde se encuentra el archivo.

para realizar una conexion con los servidores utilice telnet o netcat especificando el puerto según su necesidad.
