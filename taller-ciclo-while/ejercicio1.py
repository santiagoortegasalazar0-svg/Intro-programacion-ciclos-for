"""
Una actividad recibe dos enteros A y B con A < B. Muestre, en orden ascendente, todos los enteros
estrictamente mayores que A y menores que B. Los extremos no se muestran. Si no hay enteros entre
ellos, informe «No hay enteros interiores».
Fórmula o relación: Cada entero consecutivo difiere del anterior en 1.
"""

A = int(input("Ingrese el primer entero: "))
B = int(input("Ingrese el segundo entero: "))

if A >= B:
    print("Error: A debe ser menor que B.")
else:
    hay_enteros = False
    for i in range(A + 1, B):
        print(i, end=" ")
        hay_enteros = True

    if not hay_enteros:
        print("No hay enteros interiores.")
