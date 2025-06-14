# edad = int(input(" ingrese su edad "))
# if edad >= 18 :
#     print ("es mayor de edad")
#     if edad>25 :
#         print("estas en un punto comodo de la vida")
#     else :
#         print("estas ganando experiencia")
# elif edad < 0 :
#     print("usted ni ha nacido valla descanse mientras pueda")
# elif edad < 18 :
#     print("es menor de edad")
# numeros = int(input(" ingresa un numero"))*int(input(" ingresa un segundo numero"))*int(input(" ingresa un tercer numero"))
# if numeros >= 500 :
#     print("es un numero grande")
# if numeros >= 1000 :
#     print("es un numero muy grande")
# elif numeros >= 40 :
#     print("es un numero grande")
# else :
#     print("es un numero pequeño")

#ejemplo

año_de_nacimiento = int(input(" ingrese su año de nacimiento"))

if año_de_nacimiento < 1920 :
    print("usted es de la generacion perdida ")
elif año_de_nacimiento < 1941 :
    print("usted es de la generacion cilenciosa ")
elif año_de_nacimiento < 1965 :
    print("usted es de la generacion baby boomer ")
elif año_de_nacimiento < 1980 :
    print("usted es de la generacion x ")
elif año_de_nacimiento < 2001 :
    print("usted es de la generacion y ")
elif año_de_nacimiento > 2000 :
    print("usted es de la generacion z ")
else :
    print("el dato ingresado no puede ser procesado ")