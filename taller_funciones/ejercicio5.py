"""
Cree las funciones necesarias para descuento seguido de impuesto ficticio. El descuento se calcula
sobre la base. El impuesto se calcula sobre el subtotal ya descontado, no sobre la base original. Son
reglas ficticias, no normas tributarias. El escenario pasa el retorno del descuento a la función de
impuesto y muestra subtotal y total. Contratos en orden de parámetros: Subtotal descontado: recibe
base real no negativa en pesos, descuento real de 0 a 100 por ciento y devuelve real no negativo en
pesos. Total con impuesto: recibe subtotal real no negativo en pesos, impuesto real no negativo por
ciento y devuelve real no negativo en pesos.
Fórmula o relación: Subtotal = base × (1 − descuento / 100); total = subtotal × (1 + impuesto / 100).
Cada porcentaje se divide por 100.
Ejemplo de entrada 

Base 100000; descuento 10 %; impuesto 19 % 

Ejemplo de salida
Subtotal: 90000; total: 107100 pesos

"""

def subtotal_descontado(base, descuento):
    subtotal = base * (1 - descuento / 100)
    return subtotal


def total_con_impuesto(subtotal, impuesto):
    total = subtotal * (1 + impuesto / 100)
    return total


base = float(input("Ingrese la base (en pesos): "))
descuento = float(input("Ingrese el descuento (en porcentaje): "))
impuesto = float(input("Ingrese el impuesto (en porcentaje): "))

subtotal = subtotal_descontado(base, descuento)
total = total_con_impuesto(subtotal, impuesto)

print("Subtotal:", subtotal, "pesos")
print("Total:", total, "pesos")
