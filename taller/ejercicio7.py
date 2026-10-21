"""
Se reciben N empleados, con 1 ≤ N ≤ 40. Cada registro contiene, en este orden,
identificador entero positivo único, edad entera no negativa en años y años enteros de
antigüedad entre 1 y 50. El sueldo ficticio es la suma de una base de 100 unidades monetarias,
el valor numérico de la edad y la suma de los enteros desde 1 hasta la antigüedad; toda esa
suma se divide entre los años de antigüedad. La edad y la suma de años se consideran aportes
numéricos en unidades monetarias dentro de este modelo ficticio. Informe el sueldo de cada

empleado, el total de la nómina y los identificadores con mayor y menor sueldo. En empate
conserve el primero recibido.
Fórmula o relación: Sueldo = (100 + edad + (1 + 2 + ... + antigüedad))/antigüedad.

"""
empleados = int(input("escriba la cantidad de empleados entre 1 y 40: "))
total_nomina = 0
sueldo_mayor = 0
sueldo_menor = 0
identificador_mayor = 0
identificador_menor = 0
for i in range(empleados):
    identificador = int(input(f"escriba el identificador del empleado {i + 1}: "))
    edad = int(input(f"escriba la edad del empleado {i + 1}: "))
    antiguedad = int(input(f"escriba la antigüedad del empleado {i + 1} entre 1 y 50: "))
    sueldo = (100 + edad + (antiguedad * (antiguedad + 1) // 2)) / antiguedad
    total_nomina += sueldo
    print(f"Sueldo del empleado {identificador}: {sueldo:.2f}")
    
    if i == 0 or sueldo > sueldo_mayor:
        sueldo_mayor = sueldo
        identificador_mayor = identificador
        
    if i == 0 or sueldo < sueldo_menor:
        sueldo_menor = sueldo
        identificador_menor = identificador

print(f"Total de la nómina: {total_nomina:.2f}")
print(f"Identificador del empleado con mayor sueldo: {identificador_mayor}")
print(f"Identificador del empleado con menor sueldo: {identificador_menor}")
