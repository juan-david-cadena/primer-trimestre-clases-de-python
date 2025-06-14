#1 extraccion de enteros
numeros_enteros = (1,2,3,4,5)
print (numeros_enteros[0],numeros_enteros[4])

#2 extraccion de decimales
numeros_decimales = [1.5,2.5,3.5,4.5,5.5]
print (numeros_decimales[0],numeros_decimales[4])

#3 asignacion de variables
datos_de_tupla = ("hola","mundo","conocido")
dato1,dato2,dato3 = datos_de_tupla
print (dato1,dato2,dato3, sep= "\n")

#4 suma de listas
suma = [5,10,15,20,25]
suma_de_lista = suma[0] + suma[1] + suma[2] + suma[3] + suma[4]

#5 promedio de 3 numeros 
flotantes = (1.5,2.5,3.5,)
suma_de_flotantes = (flotantes[0] + flotantes[1] + flotantes[2]) / 3
print (f"el promedio de {flotantes} es {suma_de_flotantes}")

#6 variables individuales para enteros
numeros_enteros2 = [1,2,3,4]
x1,x2,x3,x4 = numeros_enteros2
print(x1,x2,x3,x4)
#7 multiplicacion en tuplas 
multiplicacion= (100,1000)
multiplicacion1 = multiplicacion[0] * multiplicacion[1]
print(multiplicacion1)

#8 agregacion y extraccion de listas.......
agregacion = [6,4,8]
print(agregacion)
agregacion.append(input("agrega un cuarto elemento "))
print (agregacion[0],agregacion[3])

#9 suma de tuplas
suma_de_tuplas = (2,4,6)
suma_de_tuplas2 = suma_de_tuplas[0] + suma_de_tuplas[1]
print(suma_de_tuplas2)

#10 diferencia de enteros
lista_de_enteros = (2,4,6,8,100)
print (f"la diferencia entre {lista_de_enteros[0]} y {lista_de_enteros[4]} es {lista_de_enteros[0]/lista_de_enteros[4]}")

#11 suma y agregacion de tuplas
suma_de_tuplas2 = (2,4,6,8,10)
multiplicacion_tupla = suma_de_tuplas2[0] * suma_de_tuplas2[4]
tupla_lista = suma_de_tuplas2