print("VAMOS A JUGAR\n")
n = int(input("¿Cuantos vamos a jugar? "))
diccionario = {}

for i in range(n):
	nombre = input("\nIngresa un nombre: ")
	diccionario[nombre] = int(input("Ingresa un numero entero: "))

print("\nLISTA DE JUGADORES")

for elemento in diccionario:
	print("%s: %s " % (elemento, diccionario[elemento]))

valores = list(diccionario.values())
valores.sort()
print("\n Los número ordenados son:")
print(valores)
