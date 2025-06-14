#calculadora de parentesis
simbolo = input("ingrese la letra de la operacion que desee realizar ").upper()
if simbolo == "S" :
    resul = [int(input("ingrese el primer numero a sumar")), int(input(" ingrese el segundo valor a sumar "))]
    print (f"el resultado de {resul[0]} mas {resul[1]} es {resul[0] + resul[1]}")
elif simbolo == "R" :
    resul = [int(input("ingrese el primer numero a restar")), int(input(" ingrese el segundo valor a restar "))]
    print (f"el resultado de {resul[0]} menos {resul[1]} es {resul[0] - resul[1]}")
elif simbolo == "M" :
    resul = [int(input("ingrese el primer numero a multiplicar")), int(input(" ingrese el segundo valor a multiplicar "))]
    print (f"el resultado de {resul[0]} por {resul[1]} es {resul[0] * resul[1]}")
elif simbolo == "D" :
    resul = [int(input("ingrese el primer numero a dividir")), int(input(" ingrese el segundo valor a dividir "))]
    print (f"el resultado de {resul[0]} dividido {resul[1]} es {resul[0] / resul[1]}")
else :
    print("dato invalido")