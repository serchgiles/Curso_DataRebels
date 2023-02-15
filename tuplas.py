print("Esto es una tupla")
tupla = (1,"archivo", 2/3,3+4j, False)
print(tupla)

print(" ")
print("El tipo de cada elemento es:")
for elemento in tupla:
	print(str(elemento) + " : " + str(type(elemento)))

print(" ")
print("Convertimos la tupla a lista con la funcion list()")
lista = list(tupla)
print(lista)

print(" ")
print("Convertimos a un diccionario donde las llaves son 1,2,3,4,5")
diccionario = dict(zip((1,2,3,4,5),lista))
print(diccionario)
