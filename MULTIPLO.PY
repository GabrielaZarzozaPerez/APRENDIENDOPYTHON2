# Autor: Gabriela Zarzoza Perez
# Fecha de creacion: 16/09/2019

# Se ingresa un numero y se guarda una vez que es 
# convertido a int
numero=int(input("Dame un numero entero: "))
# Se guardan en valores booleanos la evaluacion 
# de totales. Si el total es cero, quier decir 
# que el numero es multiplo.
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)
# Cuando se usa and, se resuelve por verdadero si todas
# las condiciones son verdaderas. Cuando se usa or,
# se resuelve por verdadero si una condicion es
# verdadera. Los parentesis le dicen a python que
# las primeras dos condiciones van juntas y la tecera 
# es por si sola.
if ((esMultiplo3 and esMultiplo5 ) or esMultiplo7):
    print("Correcto.")
else:
    print("Incorrecto.")
