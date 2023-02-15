import numpy as np

print("Creamos un vector con valores desde el 3 al numero que representa mi edad")
miedad = 27
vector_edad = np.array(list(range(3, miedad+1)))

print(vector_edad)

print(" ")
print("Consideremos un nuevo arreglo")
arreglo = np.array(list(range(0,4))*2)
print(arreglo)

print(" ")
print("Ahora ordenamos el arreglo numérico")
arreglo.sort()
print(arreglo)
