import pandas as pd
import glob 
import os 

current = os.getcwd()
file = glob.glob( current + '/*.csv' )
file2 = glob.glob( current + '/*.xlsx' )
mmse1 = pd.read_csv( file[2], sep= ';' )
mmse2 = pd.read_excel( file2[0] )

new = pd.merge( mmse1, mmse2, on= 'Codigo' )
new.to_excel('resultado.xlsx', index=False)


# CREE UN ARCHIVO DE EXCEL CON LOS ARCHIVOS CONCATENADOS PARA VER MEJOR #
# new.to_excel('resultado.xlsx', index=False)
#########################################################################


# FUNCION PARA CONTAR EL NUMERO DE NAN EN UNA COLUMNA   
def contarColumna( dataFrame, columna= str ):
    cuantosNaN = dataFrame[columna].isna().sum()
    filasSinNan = (dataFrame.shape)[1] - cuantosNaN 
    return filasSinNan 
#####################################################

# El numero de NaN en cada columna
columnas = new.columns
for c in columnas:
    print( f"El numero de celdas que no son NaN en {c} es: {contarColumna(new, c)}" )


# Invertir el dataframe, las filas seran las columnas
traspuesta = new.transpose()
print( traspuesta )


# Dataframe del punto dos y organizar las columnas en orden alfabetico 
# lo que entendi es organizar los nombres de las columnas dependiendo de su inicial
listaOrdenAlfabetico = mmse2.columns.sort_values()
ordenAlfabetico = mmse2.reindex( columns= listaOrdenAlfabetico )
print( ordenAlfabetico )