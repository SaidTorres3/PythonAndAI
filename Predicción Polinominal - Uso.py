# Predicción del dolar según regresión polimoninial.

x = int(input("Ingrese a cuantos dias después del dia 6/Oct/2020 quieres predecir el dolar. Ej: 68: "))
x += 2446

y = (0.000000002369 * x **3) - (0.000009805 * x ** 2) + (0.01426 * x) + 11.09
resultado = y

print(resultado)