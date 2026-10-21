"""
Un vendedor tiene N ventas, con 0 ≤ N ≤ 1000, y se recibe el importe no negativo de cada
una. Informe cuántas fueron de 200 o menos, cuántas superaron 200 sin llegar a 400 y cuántas
fueron de 400 o más. Una venta pertenece a un solo grupo.
Fórmula o relación: Grupo 1: v ≤ 200; grupo 2: 200 < v < 400; grupo 3: v ≥ 400.

"""
n_ventas = int(input("escriba la cantidad de ventas entre 0 y 1000: "))
grupo1 = 0
grupo2 = 0
grupo3 = 0

for i in range(n_ventas):
    venta = float(input(f"escriba el importe de la venta {i + 1} entre 0 y 100000: "))
    if venta <= 200:
        grupo1 += 1
    elif venta < 400:
        grupo2 += 1
    else:
        grupo3 += 1

print(f"Ventas de 200 o menos: {grupo1}")
print(f"Ventas superaron 200 sin llegar a 400: {grupo2}")
print(f"Ventas de 400 o más: {grupo3}")
