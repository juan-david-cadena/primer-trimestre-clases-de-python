"""#ejercicio 1
num_user = float(input("ingrese un numero"))
num_user2 = float(input("ingrese su segundo numero a sumar"))
resultado = num_user + num_user2
print (f"la suma de ",num_user," mas ",num_user2," es igual a ",resultado)
#ejercicio 2
num_user3 = float(input("ingrese un numero"))
num_user4 = float(input("ingrese su segundo numero a restar"))
resultado2 = num_user3 - num_user4
print (f"la resta de ",num_user3," menos ",num_user4," es igual a ",resultado2)
#ejercicio 3
num_user5 = float(input("ingrese un numero"))
num_user6 = float(input("ingrese su segundo numero a multiplicar"))
resultado3 = num_user5 * num_user6
print (f"la multiplicasion de ",num_user5," por ",num_user6," es igual a ",resultado3)
#ejercicio 4
num_user7 = float(input("ingrese un numero"))
num_user8 = float(input("ingrese su segundo numero a dividir"))
resultado4 = num_user7 * num_user8
print (f"la division de ",num_user7," por ",num_user8," es igual a ",resultado4)
#ejercicio 5
nombre = input("ingrese su nombre")
apellido = input("ingrese su apellido")
print (f"hola muy buenas tardes",nombre,apellido," es un gusto conocerte ")
#ejercicio 6
nombre2 = input("ingrese su nombre")
letra = (nombre2[0:1])
print (letra)
#ejercicio 7
nombre3 = input("ingrese una palabra")
letra2 = nombre3[-1]
print(letra2)
#ejercicio 8
num_user9 = int(input("ingrese la base"))
num_user10 = int(input("ingrese la altura"))
resultado5 = num_user9 * num_user10
print (f"el area del rectangulo es de ",resultado5)
#ejercicio 9
edad = int(input("ingrese un año de nacimiento"))
resultado6 = 2025 - edad
print (f"su edad es de ",resultado6,"años")
#ejercicio 10
user = input("ingrese un nombre")
domain = input("ingrese un dominio")
print (user+"@"+domain)
#ejercicio 11
user2 = input("ingrese su nombre")
letras2 = len(user2)
print (f"su numbre tiene",letras2,"letras")
#ejercicio 12
user3 = input("ingrese una palabra")
user4 = input("ingrese su segunda palabra")
print (user3+user4)
#ejercicio 13
nombre4 = input("ingrese una palabra")
letra4 = nombre4[1]
print(letra4)
#ejercicio 14
nombre5 = input("ingrese una palabra")
letra5 = nombre5[0:3]
print(letra5)
#ejercicio 15
nombre6 = input("ingrese una palabra")
letra6 = nombre6[::-1]
print(letra6)
#ejercicio16
num_user16 = float(input("ingrese un numero"))
num_user17= float(input("ingrese su segundo numero"))
ressuma = num_user16 + num_user17
resresta = num_user16 - num_user17
resmulti = num_user16 * num_user17
resdivi = num_user16 / num_user17
print (f"la suma de ",num_user17," mas ",num_user16," es igual a ",ressuma)
print (f"la resta de ",num_user17," menos ",num_user16," es igual a ",resresta)
print (f"la multiplicacion de ",num_user17," multiplicado ",num_user16," es igual a ",resmulti)
print (f"la division de ",num_user17," dividido ",num_user16," es igual a ",resdivi)
#ejercicio 17
num_user18 = float(input("ingrese un numero"))
operacion17 = num_user18 ** 2
print (f"el doble de {num_user18} es {operacion17}")
#ejercicio 18
num_user19 = float(input("ingrese un numero"))
operacion18 = num_user19 // 2
print (f"la mitad de {num_user19} es {operacion18}")
#ejercicio 19 
user5 = input("ingrese una frase")
user6 = len(user5)
print (f"la cantidad de caracteres de la palabra es {user6}")
#ejercicio 20 
user7 = input("ingrese una frase")
print (user7+user7+user7)
#ejercicio 21
user8 = input("ingrese su nombre")
user9 = user8 [0:2]
user10 = user8 [-2::]
print(user9," y ",user10)
#ejercicio 22
user11 = input("ingresa una frase")
user12 = len(user11)
user14 = user12 // 2
user15 = user11[user14]
print (user15)
#ejercicio 23
user16 = input("ingrese una frase")
user17 = user16 [0:10]
print(user17)
#ejercicio 24
user18 = float(input("ingrese un numero"))
user19 = user18 * user18
print (f"la elevacion de {user18} es igual a {user19}")
#ejercicio 25
user20 = float(input("ingrese un numero"))
user21 = float(input("ingrese un segundo numero"))
print ("el primer numero ingresado es mayor que el segundo?",user20 > user21)
#ejercicio 26
user25 = int(input("ingrese su edad"))
user26 = user25 * 365
print (f"usted ha vivido un total de {user26} dias ya andamos viejos")
#ejercicio 27
user28_1 = input("ingrese la palabra madre")
user28 = "m \na \nd \nr \ne"
print (user28)
#ejercicio 28
user29 = input(" ingrese una frase para ver si es mayor a 5 caracteres ")
user30 = len(user29) # el len() se usa para que el programa nos arroje la cantidad de varioables de una palabra
print (user30 > 5)
#ejercicio 29
user31 = float(input(" ingrese un numero "))
user32 = user31 * 10
print (f" el  resultado de multiplicar {user31} por 10 es {user32} ")"""
#ejercicio 30
user32 = input("ingrese una palabra")
print ("su palabra en mayuscula es",user32.upper) # el .upper se usa para poner textos enm mayuscula
print ("su palabra en minuscula es",user32.lower) # el .lower se usa para poner todo en minuscula