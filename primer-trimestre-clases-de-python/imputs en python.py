"""el input es el elemento que usamos para la entrada de datos de python esto le permite
al usuario interactuar cob el programa"""

numero_favorito = int(input("¿cual es tu numero favorito?"))

"""este es un perfecto ejemplo pues muestra como un input deve de estar dentro de una variable y ademas
un input siempre nos tomara el dato como texto por lo que para que nos permita ingresar numeros nos coresponde usar
int para numeros enteros o float para numeros flotantes"""

#ejercicios 

num = int(input("ingrese su base "))
num2 = int(input("ingrese su exponete"))
print ("estos numeros se deven multiplicar por ")
num3 = int(input("ingrese su segumdo numero"))
num4 = int(input("ingrese su segundo exponente"))
respuesta = num ** num2
respuesta2 = num3 ** num4
respuesta3 = respuesta * respuesta2
print (f"el resultado de la operacion es igual a", respuesta3)
