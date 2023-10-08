# Definir variables de diferentes tipos
cadena = "Hola"
entero = 31
flotante = 3.1
boleano = True

# Concatenar variables y guardar el resultado en una variable
resultado = cadena + str(entero) + " " + str(flotante) + str(boleano)


# Investigación sobre los límites de enteros y flotantes en Python
"""Los enteros en Python no tienen un
 límite específico, pero están limitados 
 por la memoria de la computadora."""
"""Los flotantes en Python siguen el 
 estándar IEEE 754 de punto flotante de
  doble precisión y tienen un límite de alrededor de 1.8 x 10^308."""


# Fórmula de la suma de los primeros n números pares
n = 5  # Cambiar el valor de n según sea necesario
suma_pares = n * (n + 1)


# Imprimir los resultados
print("Cadena:", cadena)
print("Entero:", entero)
print("Flotante:", flotante)
print("boleano:", boleano)
print("Resultado de concatenación:", resultado)
print("Suma de los primeros", n, "números pares:", suma_pares)
