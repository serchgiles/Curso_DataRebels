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

suma = montos.sum()
if suma >=1000:
	print("El monto es mayor a $1000. Recibes un descuento del 10%")
	suma = suma*0.9

print("El precio total a pagar es: $ %s" % round(suma,2))
