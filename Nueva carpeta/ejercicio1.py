import pandas as pd
import glob
import os   

current = os.getcwd()
file = glob.glob( current + '/*.csv' )
mmse = pd.read_csv( file[0], sep= ';' )

mmse.sort_values( 'Edad en la visita', inplace= True, ascending= False )
mmse.reset_index( inplace= True )
mmse.drop( 'index', axis = 1, inplace= True )
print( mmse )



