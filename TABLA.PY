# Autor: Gabriela Zarzoza Perez
# Fecha de creacion: 16/09/2019

numero=input("Dame un numero del 1 al 9")
numero=int(numero)
# for realiza una serie de codigo de un numero elegido
# de veces,  cuando se pide que recorra un establecimiento de 
# valores. El segundo comando de range no se incluye en la serie de valores.
#  Aqui serian los numeros del 1 al 10, o los que desees.
for i in range(1,11):
    # i va variando a cada ves que corre
    salida=" {} * {} = {}" 
    print(salida.format(numero,i,i*numero)) 
