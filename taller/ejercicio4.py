"""
Una inversión ficticia inicia con capital C no negativo y mantiene una tasa anual
porcentual I con 0 < I < 100. Se recibe también un entero M entre 0 y 50. El interés de cada año

es el saldo al comienzo de ese año multiplicado por I y dividido entre 100; se suma al saldo al
final del año. Determine el saldo después de M años; con M = 0 conserva el capital inicial.
Fórmula o relación: Saldo nuevo = saldo anterior × (1 + I/100).

"""
capital = float(input("escriba el capital inicial de la inversion entre 0 y 100000: "))
tasa = float(input("escriba la tasa de interes anual entre 0 y 100: "))
años = int(input("escriba la cantidad de años de la inversion entre 0 y 50: "))

saldo = capital
for i in range(años):
    saldo = saldo * (1 + tasa / 100)
print(saldo)
