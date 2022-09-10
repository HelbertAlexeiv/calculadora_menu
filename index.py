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
print("1. Restar (El primero menos el segundo)")
print("1. Multiplición (El primero por el segundo)")
print("1. Division (El primero sobre el segundo)")
print("1. Potenciación (El primero a la potencia del segundo)")
print("1. Logaritmo (El logaritm del primero)")

opcion = input("Dame la opción:")
