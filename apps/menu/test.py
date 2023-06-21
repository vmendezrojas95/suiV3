# test logico matematico



# Pablo, Marcelo y sofia hicieron un total de 20 empanadas. Marcelo hizo 3 veces mas que pablo y sofia hizo el doble que marcelo, cuantas empanadas hizo pablo?

# respuesta: 2


# cuantos numeros con el digito 6 hay entre 1 y 1200?

# respuesta: 300



def test_2():
    contador = 0
    for i in range(1, 1201):
        if '6' in str(i):
            contador += 1
    return contador
print(test_2())

# Una persona va al supermercado un viernes por la tarde y compra 6 bebidas de 120$ cada una, desea utilizar la promocion que mas le conviene. Que promocion le resutal mas facorabl?
# 1) 3x2
# 2) 30% de descuento
# 3) 50% de descuento en la segunda unidad
# Respuesta: 3

# Un granjero tiene 20 caballos, 40 cerdos y 10 conejos. Si llamamos caballos a los cerdos, ¿cuántos caballos tendrá en realidad?
# respuesta: 40