# """Una lista es una estructura de datos que se utilizan para almacenar multiples elementos en una sola bariable es uno de los recursos mas utilizados ya que es mutable lo que significa que se le pueden cambiar sus elementos despues de ser creados ([])"""
# """p y t h o n
#    0 1 2 3 4 5
#   -1-2-3-4-5-6"""

# """las listas trabajan usandon cordenadas donde cada elemento de la lista representa una pocicion, las listas tienen ciertas caracteristicas como lo son :
# 1. los elementos mantienen el orden en el que fueron creados (ordenar)
# 2. pueden ser modificadas despues de su creacion (mutables)
# 3. pueden contener distintos tipos de datos
# 4. permite elementops duplicados"""

# # El ".appead"

# """este metodo nos permite agregar datos a la lista despues de ser creada"""

# #Ejemplos

# print ("lista de compras")

# cosas = ["leche","huevos","frijoles"]
# Falta = ["huevos","pescado","carne"]
# print(f"en la nevera hay {cosas} falta por comprar {Falta}")
# Falta.append (input("ingrese las cosas que se acabaron"))
# print (f"en la nevera hay {cosas} no te olvides de comprar {Falta} la proxima")

# print("-----------------------------------------------------------------------------------------------")

# print("lista de articulos")
# name = input("ingresa tu nombre ")
# Productos = []
# Productos.append (input("ingresa tu primer articulo"))
# Productos.append (input("ingresa tu segundo articulo"))
# Productos.append (input("ingresa tu tercer articulo"))
# print(f" {name} tu lista de compras es {Productos}")

# print("-----------------------------------------------------------------------------------------------")

# print("precio total de 3 articulos")
# Name = input("ingrese su nombre ")
# productos = []
# productos.append (float(input("ingresa el precio tu primer articulo ")))
# productos.append (float(input("ingresa el precio de tu segundo articulo ")))
# productos.append (float(input("ingresa el precio de tu tercer articulo ")))
# produc = productos[0] + productos[1] + productos[2]
# print(f"{Name} la suma total de tus articulos es de {produc}")

# print("-----------------------------------------------------------------------------------------------")

# print ("mayor y menor numero")
# numero = []
# numero.append (float(input("ingresa un numero ")))
# numero.append (float(input("ingresa un segundo numero ")))
# numero.append (float(input("ingresa un tercer numero ")))
# numero.append (float(input("ingresa un cuarto numero ")))
# print (F" el mayor numero ingresado es {max(numero)} y el menor es {min(numero)}")
"""el "max()" se usa para sacar el valor maximo de una lista mientras "min()" se usa para allar el minimo """

# insert

"""el metodo ".insert" nos permite agregar datos a pociciones especificas de una liasta desplazando los demas datos"""

list = [1,2,3,4,5,6]
print (list)
list.insert (2,"hola mundo")
print (list) #oklpok