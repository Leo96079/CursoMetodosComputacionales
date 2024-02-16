# -*- coding: utf-8 -*-
"""actividad_01_doble_factorial.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qLzZdTznucGUzBP5wy54oi3RWkh2Wot7
"""

def doble_factorial(n):
  if type(n) == int:
    fact = 1
    if n < 0:
      mensaje = "el número no puede ser negativo"
      return mensaje
    elif n > 1:
      fact = n * doble_factorial(n - 2) # Se calcula el doble factorial
    elif n == 1:
      fact = 1
    return fact
  elif type(n) == float:
    mensaje2 = "el número no puede ser real"
    return mensaje2
print("Este es un sript que calcula el doble factorial de un numero")
n = eval(input("Ingrese el numero "))
resultado = doble_factorial(n)
print(resultado)