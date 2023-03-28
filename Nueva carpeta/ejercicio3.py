import seaborn as sns
import os
import pandas as pd 
import glob 

current = os.getcwd()
file = glob.glob( current + '/*.csv' )
mmse = pd.read_csv( file[2], sep= ';' )
mmse.drop( 'Total', axis= 1, inplace= True )
print( mmse )

sns.relplot( data= mmse, kind= 'line' )












