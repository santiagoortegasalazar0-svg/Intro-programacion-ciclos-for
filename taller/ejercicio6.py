"""
Se reciben los tiempos de N ciclistas, con 1 ≤ N ≤ 20, sobre una vuelta de 250 metros.
Cada registro contiene identificador entero positivo único, minutos enteros no negativos,
segundos entre 0 y 59 y centésimas entre 0 y 99. Cada tiempo total es positivo. Informe la
velocidad media de cada ciclista en kilómetros por hora y el identificador del ganador. En
empate de tiempo gana el primero recibido.
Fórmula o relación: Tiempo en segundos T = 60 × minutos + segundos + centésimas/100;
velocidad = 900/T. Menor T determina el ganador.
"""

total_ciclistas = int(input("escriba la cantidad de ciclistas entre 1 y 20: "))
ganador = 0
for i in range(total_ciclistas):
    identificador = int(input(f"escriba el identificador del ciclista {i + 1}: "))
    minutos = int(input(f"escriba los minutos del ciclista {i + 1}: "))
    segundos = int(input(f"escriba los segundos del ciclista {i + 1}: "))
    centésimas = int(input(f"escriba las centésimas del ciclista {i + 1}: "))
    tiempo = 60 * minutos + segundos + centésimas / 100
    velocidad = 900 / tiempo
    print(f"Velocidad del ciclista {identificador}: {velocidad:.2f} km/h")
    if ganador == 0 or tiempo < ganador:
        ganador = tiempo
        identificador_ganador = identificador

print(f"Identificador del ganador: {identificador_ganador}")
