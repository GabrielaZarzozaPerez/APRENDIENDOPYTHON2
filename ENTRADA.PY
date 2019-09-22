# Autor: Gabriela Zarzoza Perez
# Fecha de creacion: 16/09/2019

entrada=input()
print(type(entrada))
# La variable booleana verifica si lo 
# ingresado es digito, y si no detecta un punto 
# en lo igresado, lo que indicaria se que  de un 
# numero con decimales, es decir, float. Si find retorna -1
# quiere decir que lo buscado, en este caso con punto decimal
# no se encontro. (Si esEntero es True, lo capturado es entero)
esEntero=(entrada.isdigit() and entrada.find(".")==-1)
if(esEntero):
    # Se realiza si es verdadero (true)
    print("Dato entero. ¡Muy bien!")
else:
    # Se ejecutaran si la condicion es falsa (false)
    print("Dato que no es entero. Intentar nuevamente")
