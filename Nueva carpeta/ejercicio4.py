# EJERCICIO 6

import os
import glob
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

# Abrimos el archivo con pandas porque sirve para manejar dataframes
current = os.getcwd() + '\Archivos'
file = glob.glob( current + '\*.csv' )
mmse = pd.read_csv( file[2], sep= ';' )

# copiamos el archuvo y con el archivo copiado hacemos la modificacion para que no este con el total
mmse_copy = mmse.copy()
mmse_copy = mmse_copy.reset_index()
mmse_copy = mmse_copy.drop( 'Total', axis= 1 )

# Ahora vamos a graficar los datos como lo pide el problema
sns.relplot( x= 'Edad en la visita', y= 'Orientacion y Tiempo', data= mmse_copy, kind= "line", errorbar= ('ci', False), color= '#FF271F', linestyle= '--' )
sns.relplot( x= 'Edad en la visita', y= 'Orientacion y Lugar', data= mmse_copy, kind= "line", errorbar= ('ci', False), color= '#FF271F', linestyle= '--' )
sns.relplot( x= 'Edad en la visita', y= 'Memoria de fijacion', data= mmse_copy, kind= "line", errorbar= ('ci', False), color= '#FF271F', linestyle= '--' )
sns.relplot( x= 'Edad en la visita', y= 'Memoria de Evocacion', data= mmse_copy, kind= "line", errorbar= ('ci', False), color= '#FF271F', linestyle= '--' )
plt.show()







