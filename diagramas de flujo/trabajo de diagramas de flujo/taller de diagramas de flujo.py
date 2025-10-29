#ejercicio con condicionales y operaciones matematicas multiples  
#1
numero=float(input("ingrese un numero "))
if numero < 0 :
    print("el numero ingresado es negativo")
elif numero== 0 :
    print("el numero ingresado es cero")
else :
    print ("el numero es positivo")
#2
num1,num2 = int(input("ingresa un numero")),int(input("ingresa un segundo numero"))
resul = (num1 * (num1 > num2)) + (num2 * (num2 > num1))
print (f"el mayor de los numeros ingresados es {resul}")
#3
numero_par = int(input("ingrese un numero "))
numero_par_proceso = (numero_par // 2) * 2
if numero_par_proceso == numero_par :
    print ("el numero es par")
else :
    print("el numero es impar")
#4
nume = int(input("ingrese un numero "))
if nume >= 10 and nume <=20 : 
    print ("el numero esta entre 10 y 20")
else :
    print("El numero no esta entre 10 y 20")
#5
nume1,nume2,nume3 = int(input("ingresa un numero")),int(input("ingresa un segundo numero")),int(input("ingresa un tercer numero"))
if nume1 > nume2 and nume1 > nume3 :
    print(f"el numero {nume1} es el mayor de todos")
elif nume2 > nume1 and nume2 > nume3 :
    print(f"el numero {nume2} es el mayor de todos")
else :
    print(f"el numero {nume3} es el mayor de todos")
#6
la_mari = [int(input("ingresa el precio del primer producto")),int(input("ingresa el precio del segundo producto")),int(input("ingresa el precio del tercer producto")),]
la_marit = la_mari[0] + la_mari[1] + la_mari[2]
if la_marit < 100:
    print(f"el precio de sus productos con descuento incluido es de {((10 / 100) * la_mari) - la_mari}")
else:
    print(f"el precio de su producto es {la_mari}")
    
#7
edd = int(input("ingrese su edad "))
if edd >= 18:
    print("usted es mayor de edad, usted purde votar")
else :
    print("usted no puede votar")
#8 
dinero = float(input("ingrese el total de su compra "))
cliente = input("usted es vip, ¿si o no? ")
j = cliente.upper()
if j == "SI":
    print(f"su total es de {dinero - ((20 / 100) * dinero) } que tenga un buen dia")
else :
    print(f"su total es {dinero} que tenga un buen dia")
#9
f = int(input("ingresa un numero "))
n = (5 * (f // 5)) - (3*(f // 3))
if n == 0:
    print(f"el numero {f} es multiplo de 3 y 5")
else :
    print("el numero ingresado no es multiplo de 3 y 5")
#10 
numero_dado = int(input("ingresa un numero "))
verifi = int(input("ingrese el numero ha verificar si es divisible "))
verifi2 = int(input("ingrese el segundo numero ha verificar si es divisible "))
operacion7 = (verifi * (numero_dado // verifi)) - (verifi2*(numero_dado // verifi2))
if operacion7 == 0:
    print(f"el numero {numero_dado} es divisible entre {verifi} y {verifi2}")
else :
    print(f"el numero {numero_dado} no es divisible entre {verifi} y {verifi2}")
#11
la_lista = [int(input("ingresa un numero ")),int(input("ingresa otro numero ")),int(input("ingresa otro numero ")),int(input("ingresa otro numero ")),int(input("ingresa otro numero "))]
if la_lista[2] > 10 :
    print("es mayor a 10")
else :
    print("no es menor o igual a 10")
#12
if la_lista[0] == 7:
    print("el 7 sa halla en la lista")
elif la_lista[1] == 7:
    print("el 7 sa halla en la lista")
elif la_lista[2] == 7:
    print("el 7 sa halla en la lista")
elif la_lista[3] == 7:
    print("el 7 sa halla en la lista")
elif la_lista[4] == 7:
    print("el 7 sa halla en la lista")
else:
    print("el 7 no se halla en la lista")
#13
suma_lista = la_lista[0] + la_lista[1]
if suma_lista > 10:
    print("la suma es alta")
else :
    print("la resta es menor ")
#14
nombres = [(input("ingresa un nombre ")),(input("ingresa otro nombre ")),(input("ingresa otro nombre ")),(input("ingresa otro nombre ")),(input("ingresa otro nombre "))]
print (nombres[4])
if nombres[-1] == "marta":
    print("nombre correcto")
else :
    print("nombre diferente ")
#15
sonic_colors = [(input("ingresa un color ")),(input("ingresa otro color ")),(input("ingresa otro color "))]
if sonic_colors[1]  == "azul":
    sonic_colors[1] = "verde"
else :
    print(sonic_colors)
#16
t =  (int(input("ingrese un numero ")),int(input("ingrese un numero ")),int(input("ingrese un numero ")),int(input("ingrese un numero ")),int(input("ingrese un numero ")))
if t[0] > t[-1]:
    print("Orden hacendente")
else:
    print("Orden decendente ")
#17
if t[1] > 30 :
    print("edad mayor a treinta")
else :
    print("edad menor o igual a 30")
#18
tu = list(t)
if tu[1] == 2:
    tu[1] = 10
hol = tuple(tu)
print(hol)
#19
if hol[1] > 5 :
    print("cordenada alta")
else :
    print("cordenada baja")
#20
#ejercisio20
tupla1 = (int(input("ingresa un numero")),int(input("ingresa un segundo numero")),int(input("ingresa un tercer numero")))
tupla2 = (int(input("ingresa un numero para la segunda tupla")),int(input("ingresa un segundo numero")),int(input("ingresa un tercer numero")))
if tupla1 == tupla2 :
	print("tuplas iguales ")
else :
	print("tuplas diferentes")
#ejercisio21
datos_personales = {"nombre4" : input("ingrese su nombre "), "edad" : int(input("ingrese su edad "))}
if datos_personales["edad"] >= 18 :
	print(f"hey {datos_personales['nombre4']} usted es mayor de edad")
else :
	print(f"hey {datos_personales['nombre4']} usted es menor de edad")# 
#ejercicio22
datos_personales2 = {"nombre4": input("ingrese su nombre "), "edad": int(input("ingrese su edad "))}
if datos_personales2["edad"] >= 18:
    datos_personales2["edad"] = 21
    print(datos_personales2)
else:
    print(datos_personales2)
#ejercicio23
datos_vivienda = {
    "nombre2" : input("ingrese su nombre"),"edad": int(input("ingresa tu edad ")) 
}
datos_vivienda ["ciudad"] = "bogota"
print (datos_vivienda)
#ejercicio24
caso24 = {"producto": input("ingresa el nombre de un producto "), "precio": 1200}
if "precio" in caso24 :
    print(f"el precio de {caso24['producto']} es de {caso24['precio']}")
else :
    print("producto no disponible")
#ejercicio25
caso25 = {"pan": 1200, "leche": 2000}
caso25_1 = input("ingrese un producto ")
if caso25_1 in caso25 :
    print (f"el producto {caso25_1} cuesta {caso25[caso25_1]}")
else :
    print("producto no disponible")
