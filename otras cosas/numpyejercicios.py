import numpy as np

################## EJERICIO 1 ##################
new_matriz_ceros = np.zeros( (3, 4), dtype= int )
# print( new_matriz_ceros )

new_matriz_uno = np.zeros( (3, 4), dtype= int )
new_matriz_uno[0:1] = 1
# print(new_matriz_uno)

new_matriz_rango = np.zeros( (3, 4), dtype= int )
rango = np.arange( 5,9 )
new_matriz_rango[2:3] = rango
# print( new_matriz_rango )

################## EJERICIO 2 ##################
vector = np.zeros( 10 )
for i in range( 10 ):
    if i % 2 == 0:
        vector[i] = 2
    else:
        vector[i] = 1
# print( vector )

tablero = np.zeros( (8, 8), dtype= int )
tablero[ 1::2, 0::2 ] = 1 # se salta en las filas
tablero[ 0::2, 1::2 ] = 1 # se Salta en las columnas

print( tablero )

################## EJERICIO 3 ##################
matriz_random = np.random.rand( 5, 5 )
min = matriz_random.min()
max = matriz_random.max()
# print( matriz_random )
# print( f"Valor maximo: {max}, valor minimo: {min}" )

matriz_random = (matriz_random - min) / (max - min)
# print( "Matriz normalizada" )
# print( matriz_random )


