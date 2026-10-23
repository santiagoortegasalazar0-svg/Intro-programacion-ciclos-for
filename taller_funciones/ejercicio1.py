"""
Cree una función para área de un triángulo por base y altura. La altura es perpendicular a la base.
Use dos llamadas y muestre las dos áreas y su suma, calculada con los retornos. Contrato: Área de un
triángulo por base y altura: recibe base y altura, reales positivos expresados en centímetros y devuelve
el área real en centímetros cuadrados.
Fórmula o relación: Área = base × altura / 2. La división entre 2 obtiene la mitad del rectángulo de
igual base y altura.

"""

def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

base1 = float(input("Ingrese la base del primer triángulo (cm): "))
altura1 = float(input("Ingrese la altura del primer triángulo (cm): "))

base2 = float(input("Ingrese la base del segundo triángulo (cm): "))
altura2 = float(input("Ingrese la altura del segundo triángulo (cm): "))

area1 = area_triangulo(base1, altura1)
area2 = area_triangulo(base2, altura2)

print("Área del primer triángulo: ", area1,  "cm²")
print("Área del segundo triángulo: ", area2, "cm²")
print("Suma de las áreas: ", area1 + area2, "cm²")