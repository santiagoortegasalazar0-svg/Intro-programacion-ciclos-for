"""
Se conoce el primer término A, la diferencia D y la cantidad N de términos de una
progresión. A y D son enteros entre -100 y 100, y N está entre 0 y 1000. Determine la suma de
los N términos; si N es cero, el total es cero.
Fórmula o relación: t1 = A; tk+1 = tk + D; S = t1 + t2 + ... + tn.

"""
primer_termino = int(input("escriba el primer termino de la progresion entre -100 y 100: "))
diferencia = int(input("escriba la diferencia de la progresion entre -100 y 100: "))
cantidad_terminos = int(input("escriba la cantidad de terminos de la progresion entre 0 y 1000: ")) 

total = 0
for i in range(cantidad_terminos):
    total += primer_termino + i * diferencia
print(total)

