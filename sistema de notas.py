#calculadora de notas
nom = input("ingresa tu nombre: ")
nota1 = float(input("ingrese su primera nota: "))
nota2 = float(input("ingrese su segunda nota: "))
nota3 = float(input("ingrese su tercera nota: "))
problema = nota1 * 0.20
problema2 = nota2 * 0.30
problema3 = nota3 * 0.50
solucion = problema + problema2 + problema3
if solucion == 3.4 :
    print(f" ",nom,"tu nota final es de ",solucion,"mero salado pa sacar 3.4")
elif solucion < 3.4 :
    print(f" ",nom,"tu nota final es de ",solucion,"en la casa le pegan hoy")
else :
    print(f" ",nom,"tu nota final es de ",solucion,)
