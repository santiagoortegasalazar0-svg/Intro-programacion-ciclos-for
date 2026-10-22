"""
Una actividad recibe ternas de capital C, tasa anual I y cantidad entera de años M. Una terna solo
se acepta si C es no negativo, 0 < I < 100 y M es positivo. Las ternas inválidas se descartan y se recibe
otra completa; el flujo garantiza una terna válida. Para la primera terna válida, muestre el saldo al
terminar cada año y el saldo final. Los intereses se incorporan al saldo una vez por año. La tasa I se
ingresa como porcentaje. Cada interés anual es el saldo anterior multiplicado por I y dividido entre 100;
el nuevo saldo es el saldo anterior más ese interés. Capital y saldos se expresan en una misma unidad
monetaria.
Fórmula o relación: Saldo inicial = C. Saldo del año siguiente = saldo anterior × (1 + I / 100).

"""

while True:
    C = float(input("Ingrese el capital inicial (no negativo): "))
    I = float(input("Ingrese la tasa anual (0 < I < 100): "))
    M = int(input("Ingrese la cantidad de años (positivo): "))

    if C >= 0 and 0 < I < 100 and M > 0:
        break
    else:
        print("Datos inválidos. Intente nuevamente.")

saldo = C
for año in range(1, M + 1):
    interes = saldo * I / 100
    saldo += interes
    print(f"Saldo al final del año {año}: {saldo:.2f}")
print(f"Saldo final: {saldo:.2f}")

