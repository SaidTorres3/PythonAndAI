lista = list(range(2000,2051))

resultado = []

for x in lista:
    # y = ((0.0000000005923 * (x**4)) - (0.00000326 * (x**3)) + (0.007129 * (x**2)) + (11.09 * x)) INTEGRAL
    # y = ( (0.00000000710 * (x**2)) + (0.00001961 * x) + (0.01426) ) DERIVADA

    y = ( (x * ((71*(x**3))/30000000000) + ((1961 * (x**2))/200000000) + ((713*x)/50000) ) / 30000000000) + 12
    resultado.append(y)

print(resultado)