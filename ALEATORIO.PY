# Autor: Gabriela Zarzoza Perez
# Fecha de creacion: 16/09/2019

# Para poder usar una funcion en un programa, primero debe 
# importarse, usando la palabra import.
import random

# Se define una variable float, y se le agreaga el valor deseado. 
numero1=float(10.5)

# En python, una funcion es un conjunto de instrucciones que 
# procesan una tarea especifica, como un plan a realizar.
# Se declara con def. todo el codigo escrito en la parte derecha 
# de la definicion, y forma parte de la funcion 
def miFuncion():
    # Se pasa a float el numero al azar que sale en 
    # random.randrange() (solo si esta disponible si se importa 
    # la funcion random (palabra random(librerias)) 
    numero2=float(random.randrange(1,10)) 
    # Se utilizan meta sustituciones para mostrar resultados.
    mensaje="La suma de {} y {} es {}" 
    print(mensaje.format(numero1,numero2,numero1+numero2))

# Se ejecuta la funcion definida en el codigo 
miFuncion()
