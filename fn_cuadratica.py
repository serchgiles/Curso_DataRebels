from cmath import sqrt as csqrt
from math import sqrt

def fn_cuadratica(a,b,c):
	delta = b**2 - 4*a*c
	if a == 0 and b == 0:
		print("Sin soluciones")
		return([None, None])
	elif a == 0 and b != 0:
		print("Solo una solucion")
		x1=(-1)*c/b
		return([x1, None])
	elif delta < 0:
		print("Soluciones Imaginarias")
		x1 = ((-1)*b + csqrt(delta))/(2*a)
		x2 = ((-1)*b - csqrt(delta))/(2*a)
		return([x1, x2])
	elif delta >=0:
		print("Soluciones Reales")
		x1 = ((-1)*b + sqrt(delta))/(2*a)
		x2 = ((-1)*b - sqrt(delta))/(2*a)
		return([x1, x2])
