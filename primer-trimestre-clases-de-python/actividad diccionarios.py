#taller 1 calculadora de producto
nombre= (input("ingrese el nombre del producto "))
precio = (int(input("ingrese el precio unitario del producto ")))
The_list = [nombre,precio,int(input("ingrese la cantidad del producto "))]
el_producto = {"Producto" : The_list,}
print(f"El costo total de {nombre} es {The_list[2] * precio}")

#taller 2 factura de multiples productos

productos1 = [(input("ingrese el nombre del producto ")),int(input("ingrese el precio del producto")),int(input("ingresa la cantidad del producto"))]
productos2 = [(input("ingrese el nombre del segundo producto ")),int(input("ingrese el precio del segundo producto")),int(input("ingresa la cantidad del segundo producto"))]
productos3 = [(input("ingrese el nombre del tercer producto ")),int(input("ingrese el precio del tercer producto")),int(input("ingresa la cantidad del tercer producto"))]
#para ahorrar codigo y saltarme tener que crear variables para el ingreso de los datos,almacenar cada producto como tupla y agregar cada producto en una lista con su cantidad intoduje todo en una sola bariable que seria su resultado sinal
print(f"el precio total de {productos1[0]} es de {productos1[1] * productos1[2]} y el precio total de {productos2[0]} es de {productos2[1] * productos2[2]} y el precio total de {productos3[0]} es de {productos3[1] * productos3[2]}")

#taller 3 registro de notas de un estudiante
nombres = input("ingrese su nombre")
asicnatura1 = (input("ingrese el nombre de la asignatura"),float(input("ingresa la primera nota de esa materia")), float(input("ingresa la segunda nota de esa materia")))
asicnatura2 = (input("ingrese el nombre de la asignatura"),float(input("ingresa la primera nota de esa materia")), float(input("ingresa la segunda nota de esa materia")))
asicnatura3 = (input("ingrese el nombre de la asignatura"),float(input("ingresa la primera nota de esa materia")), float(input("ingresa la segunda nota de esa materia")))
la_lista= [asicnatura1,(asicnatura1[1] + asicnatura1[2]) / 2,asicnatura2,(asicnatura2[1] + asicnatura2[2]) / 2,asicnatura3,(asicnatura3[1] + asicnatura3[2]) / 2]
DICCIONARI = {"nombre" : nombre, "materias" : asicnatura1[0] and asicnatura2[0] and asicnatura3[0]}
promedio = la_lista