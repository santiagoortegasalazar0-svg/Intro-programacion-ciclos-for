"""
Cree una función para pago semanal con horas extra. Es un modelo ficticio: las primeras 40 horas
se pagan a la tarifa ordinaria; solo las horas que exceden 40 se pagan a 1,5 veces esa tarifa. Llame para
dos personas y sume los retornos, sin redondearlos antes de sumar. Contrato: Pago semanal con horas
extra: recibe horas semanales reales no negativas y tarifa real no negativa en pesos por hora y devuelve
el pago real semanal en pesos.
Fórmula o relación: Pago = horas × tarifa si horas ≤ 40; si horas > 40, pago = 40 × tarifa + (horas −
40) × tarifa × 1,5.

"""

def pago_semanal(horas, tarifa):
    if horas <= 40:
        pago = horas * tarifa
    else:
        pago = 40 * tarifa + (horas - 40) * tarifa * 1.5
    return pago

persona1_horas = int(input("Ingrese las horas trabajadas por la primera persona: "))
persona1_tarifa = float(input("Ingrese la tarifa por hora de la primera persona (en pesos): "))
persona2_horas = int(input("Ingrese las horas trabajadas por la segunda persona: "))
persona2_tarifa = float(input("Ingrese la tarifa por hora de la segunda persona (en pesos): "))


pago1 = pago_semanal(persona1_horas, persona1_tarifa)
pago2 = pago_semanal(persona2_horas, persona2_tarifa)
total = pago1 + pago2

print("Pagos:", pago1, "y", pago2, "pesos; total:", total)


