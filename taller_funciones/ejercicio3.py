"""
Cree las funciones necesarias para tolerancia de una medición. Debe reutilizar una función de
valor absoluto que recibe un real y devuelve su distancia al cero. Los extremos de tolerancia se aceptan.
La función de aceptación utiliza el retorno de valor absoluto. El escenario consulta dos mediciones por
separado. Contratos en orden de parámetros: Valor absoluto: recibe real finito y devuelve real no
negativo. Aceptación: recibe medición y objetivo reales, tolerancia real no negativa y devuelve lógico.
Fórmula o relación: Error = valor absoluto de (medición − objetivo); aceptable cuando error ≤
tolerancia.

"""

def valor_absoluto(x):
    if x < 0:
        return -x
    else:
        return x

def aceptacion(medicion, objetivo, tolerancia):
    error = valor_absoluto(medicion - objetivo)
    return error <= tolerancia

objetivo = float(input("Ingrese el valor objetivo: "))
tolerancia = float(input("Ingrese la tolerancia: "))

medicion1 = float(input("Ingrese la primera medición: "))
medicion2 = float(input("Ingrese la segunda medición: "))

aceptable1 = aceptacion(medicion1, objetivo, tolerancia)
aceptable2 = aceptacion(medicion2, objetivo, tolerancia)

print("La primera medición es aceptable:", aceptable1)
print("La segunda medición es aceptable:", aceptable2)

