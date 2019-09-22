# Autor: Gabriela Zarzoza Perez
# Fecha de creacion: 16/09/2019

# Se define una variable str, con una cadena de digitos
numero="1234"
# Se muestra el tipo que tiene la variable. La salida de type()
# no es un str es un dato type.
print(type(numero))
# Se convierte la cadena a su equivalencia int (osea el valor que le quieras agregar).
numero=int(numero)
# Se muestra como el tipo a cambiado aunque se usa la misma 
# variable 
print(type(numero))
# Se declara un str con neta sustitucion (posiciones donde iran
# los valores proporcionados usando formato) (aqui se hacen las operaciones)
salida="El numero utilizado es{}"
# La neta sustitucion hara que donde esta 
# {} se coloque el valor del numero.(resultado final, aqui se muestra)
print(salida.format(numero))
