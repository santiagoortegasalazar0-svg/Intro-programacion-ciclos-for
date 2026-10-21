"""
Una empresa tiene N empleados, con 0 ≤ N ≤ 1000. Se recibe el sueldo no negativo de
cada empleado y se desea el total de la nómina. Para una empresa sin empleados, el total es
cero.
Fórmula o relación: Nómina = sueldo1 + sueldo2 + ... + sueldo n.
"""


n_empleados = int(input("escriba la cantidad de empleados entre 0 y 1000: "))
nomina = 0
for valor in range(n_empleados):
    sueldo = float(input(f"escriba el sueldo del empleado {valor + 1} entre 0 y 100000: "))
    nomina += sueldo
print(nomina)
