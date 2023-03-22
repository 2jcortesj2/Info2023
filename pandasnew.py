import  numpy as np
import pandas as pd
import os
import glob

s = pd.Series( np.random.randn(5), index= ['a', 'b', 'c', 'd', 'e'] ) # el index es donde van los indices 
print( s )
print( s[0] )
print( s[:3] )


d = d = {"a": 0.0, "b": 1.0, "c": 2.0}
e = pd.Series(d, index=["b", "c", "d", "a"])
print( e )

# OPERACIONE O CAMBIO DE ORDEN EN LA SERIE
print( e.median() ) # me retorna el valor que esta justo en la mitad de los datos

print( s[ [4, 3, 1] ] ) # para cambiar el orden en el que se imprimen las cosas

# PARA OBTENER LA MATRIZ QUE RESPALDA LA SERIE
print( s.array )

# pasar a ndarray real
print( s.to_numpy )


# PARA OBTENER EL VALOR DE UN INDICE EN UNA SERIE, SE HACE DE LA MISMA MANERA QUE CON UN DICCIONARIO
print( s["a"] )
print( s.get( "j", "No se encuentra en la serie" ) ) # si encuentra el valor devuelve que hay en el, si no, devuelve lo que le inserte en la segunda posicion


# OPERACIONES
print( s + s ) 
# tambien se puede multiplicar, dividir, entre otras operaciones

print( "" )
print(np.exp( s )) # euler ** s

withnan = s[1:] + s[:-1] # Deja el primer y el ultimo lugar con nan
withoutnan = withnan.dropna() # quita los nan que hayan en la serie
print( withnan )
print( withoutnan )

current = os.getcwd()
file = glob.glob( current + '/*.csv' )
#print( current )
mmse = pd.read_csv( file[0], sep= ';' )

# print( mmse ) Me imprime la tabla completa

# METODOS QUE SE PUEDEN APLICAR A LAS TABLAS
print(mmse.size) # Me muestra el tamaño de la tabla
print(mmse.columns) # Me muestra las columnas que tenga la tabla

mmse['Sexo'] # muestra las columnas del sexo
print(mmse['Escolaridad'].describe()) # imprime las estadisticas varias de escolaridad

print( mmse['Escolaridad'].max() ) # valor maximo de la columna "Escolaridad"

print( mmse['Escolaridad'].mean() ) # Devuelve la media aritmetica de la colimna



mmse_copy = mmse.copy()
mmse_copy.reset_index()
#print( mmse_copy ) # [ 23 rows x 11 colums ]

# mmse_copy = mmse_copy.drop( ['index'], axis= 1 )
# del mmse_copy['index']


mmse_copy = mmse_copy.assign( hola= np.random.rand(23) )
mmse_copy = mmse_copy.set_index( 'hola' )
print( mmse_copy )
print( mmse_copy.index )

print(mmse.iloc[0]) # para obtener un dato de la tabla se pone la posicion, solamente en posiciones enteras
# mmse.loc["posicion particular"] cuando no son enteros, es deci , pueden ser float o strings o combinados

# TENGO UNA DUDA CON EL METODO SHAPE
# falto el metodo .where y .mask














