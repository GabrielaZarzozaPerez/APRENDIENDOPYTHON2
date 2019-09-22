# Autor: Gabriela Zarzoza Perez
# Fecha de creacion: 16/09/2019

numero1=input("Numero 1:")
numero2=input("Numero 2:")
salida="Numeros proporcionados: {} y {}. {}. "
if (numero1==numero2):
    # Si los numeros capturados son iguales, aqui dice.
    print(salida.format(numero1,numero2,"Los numeros son iguales"))
else:
    # Condicionales anidadas, if dentro de otro if.
    # Si los numeros no son iguales, avisa si el primero es mayor
    # que el segundo o viceversa.s
    if numero1>numero2:
        # Reporta si el primer numero es mayor al segundo.
        print(salida.format(numero1, numero2, "El mayor es el primero"))
    else:
        # o de lo contario, si el primero no es mayor al segundo.
        print(salida.format(numero1, numero2, "El mayor es el segundo"))
