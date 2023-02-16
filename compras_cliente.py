import numpy as np

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print("INGRESE LOS MONTOS DE LAS COMPRAS\n")

x = 1
montos = np.array([])
while x > 0:
	x = "e"
	while not isfloat(x):
		x = input("Ingrese un monto: $")
		if not isfloat(x):
			print("Ingresa un monto valido")
		elif float(x) <0:
			print("Ingresa un monto positivo o un cero para terminar")
			x = "w"
	x = float(x)
	montos = np.append(montos,[x])

print("La suma de los montos es %s" % round(montos.sum(),2))
