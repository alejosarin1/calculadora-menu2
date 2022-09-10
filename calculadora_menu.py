# calculadora con menu

import math


from math import log

print("------------------------------------")
print("--------Calculadora - Menu----------")
print("------------------------------------")

x= float(input("dame el valor del numero x :"))
y= float(input("Dame el valor del numero y :"))

print("\nDame la opcion que deseas realizar : \n")
# se despliega el menu para seleccionar la opccion que deseas realizar:
print("1. Sumar(El primero mas el segundo)")
print("2. restar(El primero menos el segundo)")
print("3. Multiplicar(El primero multiplicado por  el segundo)")
print("4. Dividir.(El primero sobre  el segundo)")
print("5. Potencia(El primero a la potencia del segundo)")
print("6. Logaritmo(El Logari del primero)")

opcion = input("\nDame la opcion")