"""
Cree una función para precio unitario comparable. Dos paquetes pueden tener tamaños distintos;
no compare solo sus precios totales. Llame para dos paquetes y use los retornos para indicar el más
económico por gramo; si coinciden indique igualdad. Contrato: Precio unitario comparable: recibe
precio total real no negativo en pesos y cantidad real positiva en gramos y devuelve el precio real de un
gramo en pesos.
Fórmula o relación: Precio por gramo = precio total / cantidad de gramos.

"""

def precio_unitario(precio_total, cantidad_gramos):
    precio_por_gramo = precio_total / cantidad_gramos
    return precio_por_gramo

precio1 = float(input("Ingrese el precio total del primer paquete (en pesos): "))
cantidad1 = float(input("Ingrese la cantidad de gramos del primer paquete: "))

precio2 = float(input("Ingrese el precio total del segundo paquete (en pesos): "))
cantidad2 = float(input("Ingrese la cantidad de gramos del segundo paquete: "))

precio_por_gramo1 = precio_unitario(precio1, cantidad1)
precio_por_gramo2 = precio_unitario(precio2, cantidad2)

print("Precio por gramo del primer paquete: ", precio_por_gramo1, "pesos")
print("Precio por gramo del segundo paquete: ", precio_por_gramo2, "pesos")

if precio_por_gramo1 < precio_por_gramo2:
    print("Conviene el primer paquete.")
elif precio_por_gramo2 < precio_por_gramo1:
    print("Conviene el segundo paquete.")
else:
    print("Ambos paquetes tienen el mismo precio por gramo.")

