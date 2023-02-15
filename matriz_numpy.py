import numpy as np

print("Creamos una matriz de 3x3 con valores del 0 al 8")
matriz = np.reshape(np.array(range(0,9)),(3,3))
print(matriz)

print("\nAhora una matriz identidad de 6x6 (tambien se puede crear con la funcion identity")
iden6 = np.eye(6)
print(iden6)
