# Autor: Gabriela Zarzoza Perez
# Fecha de creacion: 16/09/2019

numero=str("")

# Cuando escribes True como condicion de while, creas un 
# ciclo infinito que no deja de trabajar hasta que  
# tu le indiques con la instruccion break, entoces ahi para.
while True:
    numero=input("Dame un numero entero: ")
    if numero=="":
        # Si el numero es vacio, avisa y se realiza la operacion requerida.
        print("Vacio. Salida del programa.")
        break
    else:
        # Si se proporciono valor, acumulado = acumulado + numero
        # Se realiza el calculo usando suma incluyente (+=)
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))
