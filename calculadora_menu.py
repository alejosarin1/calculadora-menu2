# calculadora con menu

import math


from math import log

print("------------------------------------")
print("--------Calculadora - Menu----------")
print("------------------------------------")
bandera=False
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

opcion = int(input("\nDame la opcion : "))

#procesing
if (opcion== 1):
    z= x+y
    print(x,"+",y)
elif (opcion== 2):
    z=x-y
    print(x,"-",y)
elif(opcion== 3):
    z=x*y
    print(x,"*",y)
elif(opcion==4):
    z=x/4
    print(x,"/",y)
elif(opcion==4 and y==0):
    print("El denomidador es igual a cero y ")
    print("No se puede realizar la operacio")
    bandera=True
elif(opcion== 5):
    z=pow(x,y)
    print(x,"expo",y)
elif(opcion==6):
    z=log(x) 
    print("Loaritmo de ",x)
elif(opcion== 6 and x<= 0 ):
    print("No se puede calcular el logaritmo")
    bandera= True
else:
    print("Opccion no valida")
# se escribe el resultado con otra condicion
if(opcion< 7 and bandera== False):
    print("Resultado :",z)