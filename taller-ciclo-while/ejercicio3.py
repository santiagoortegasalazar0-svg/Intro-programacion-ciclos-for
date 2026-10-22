"""
Un curso recibe notas entre 0 y 100, una a una, hasta recibir -99. Muestre la cantidad de notas y
su promedio. El centinela no es una nota y no participa en el cálculo. Si aparece primero, muestre
cantidad cero y «Sin notas» en lugar de un promedio. El flujo siempre contiene -99. El promedio es la
suma de las notas aceptadas dividida entre su cantidad.
Fórmula o relación: Promedio = suma de las notas / cantidad de notas, solo cuando la cantidad sea
positiva.

"""


cantidad = 0
suma = 0

while True:
    nota = int(input("Ingrese una nota: "))
    if nota == -99:
        break
    if 0 <= nota <= 100:
        suma += nota
        cantidad += 1

if cantidad == 0:
    print("Sin notas")
else:
    promedio = suma / cantidad
    print("Cantidad de notas:", cantidad)
    print("Promedio:", promedio)