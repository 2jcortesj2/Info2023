import numpy as np

a = np.arange( 63 ).reshape( 3,7, 3 )
# print(a[0][4][1]) DIMENSION
# print( a )

b = np.array( [ (1.5, 2, 3), (4, 5, 6), (1, 4, 6) ] )
# print( b )

# SHAPE
d = np.array( [ 1.3, 2, 3, 4, 5, 6 ] )
d.shape = ( 1, 2, 3 )
# print( d )

# SIZE
# print(np.size( d ))

# DTYPE
# print( a.dtype.name ) # int
# print( d.dtype.name ) # float

e = np.array( [ (1, 2), (3, 5) ], dtype= complex )
# print( e )

# para ordenar un elemento se usa sort np.sort( array que quiero organizar )
 

# tambien se pueden concatenar con np.concatenate((a, b))


# Para obtener numero aleatorios
f = np.random.rand( 3, 2 )
# print( f )

rg = np.random.default_rng( 0 )
r = rg.random( (3, 4) )
a = np.floor( 10 * r ) # multiplica por todos los numeros de la matriz
a.shape = ( 3 , 4 )
print( a )
