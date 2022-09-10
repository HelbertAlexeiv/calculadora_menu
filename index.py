#Calculadora con menú
from math import log

print("----------------------------")
print("----CALCULADORA - MENU------")
print("----------------------------")

#Input
bandera = False

x = float(input("Ingresa el valor del numero x: "))
y = float(input("Ingresa el valor del numero y: "))

print("\nDame la opción que deseas realizar: \n")

#Se despliega el menú para seleccionar la opción que deseas realizar

print("1. Sumar (El primero más el segundo)")
print("2. Restar (El primero menos el segundo)")
print("3. Multiplición (El primero por el segundo)")
print("4. Division (El primero sobre el segundo)")
print("5. Potenciación (El primero a la potencia del segundo)")
print("6. Logaritmo (El logaritm del primero)")

opcion = int(input("\nDame la opción:"))

#Processing
if opcion == 1:
    z = x + y
    print(x, "+", y)
elif opcion == 2:
    z = x - y
    print(x, "-", y)
elif opcion == 3:
    z = x * y
    print(x, "*", y)
elif opcion == 4 and y!=0:
    z = x/y
    print(x, "/", y)
elif opcion == 4 and y == 0:
    print("(y) es igual a 0")
    print("No se puede realizar la division")
    bandera = True
elif opcion == 5:
    z = pow(x, y)
    print(x, "^", y)
elif opcion == 6:
    z = log(x)
    print("Logaritmo de", x)
elif opcion == 6 and x <= 0:
    print("el valor de (x) es <= 0")
    print("no se puede calcular el logaritmo")
    bandera = True
else: 
    print("opcion no valida")
if opcion < 7:
    print("Resultado =", z)

