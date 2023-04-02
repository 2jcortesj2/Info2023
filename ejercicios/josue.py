import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

matriz = np.arange(8 * 2000 * 176).reshape( 8, 2000, 176 ) # hay 176 epocas, en cada una de estas hay 2000 muestras

new = matriz[ 0, :, 0 ]

sensores = matriz.shape[0]
puntos = matriz.shape[1]
epocas = matriz.shape[2]
print( new )
senalContinua = np.reshape( matriz, ( sensores, puntos * epocas ), order= 'F' )
juanjo = senalContinua[0, 0 : 2000]
print( juanjo )
# plt.plot(self.senalcontinua[sensor-1, self.puntos*(epoca-1):self.puntos*epoca], color=color)
#         plt.title(f'Época {epoca}, Sensor {sensor}', fontdict={'fontsize': 16, 'fontweight':'bold'})
#         plt.xlabel('Puntos')
#         plt.savefig("signal.png")
#         plt.show()

#print( nueva )

# # TODO EN GENERAL
# path = r'C:\Users\Josue Paniagua Lopez\OneDrive\Escritorio\Info2023\Info2023-3\Archivos\ArchivosMat\C002_EP_reposo.mat'
# cargar = sio.loadmat( path )
# senal = cargar['data']

# # IMPRIMIR TAMAÑO SEÑAL
# print( senal.ndim ) # dimension de la señal
# print( senal.shape ) # forma de la señal

# # GRAFICAR LA SEÑAL CONTINUA
# sensores = senal.shape[0]
# puntos = senal.shape[1]
# epocas = senal.shape[2]

# senal_continua = np.reshape( senal, ( sensores, puntos * epocas ), order= 'F' ) # no entendi nada de lo que hace esto, lo hice de muestra de la profe
# plt.subplots(1)
# plt.plot(senal_continua[0, 0:1700]) # aca solo graficamos hasta 1700 para que se entienda mas
# plt.show()

# # GRAFICAR UNA EPOCA DE UNA SEÑAL


# # GRAFICAR LA SEÑAL CON UN COLOR DETERMINADO    
# color = 'green'
# plt.subplots(1)
# plt.plot(senal[0,:,0], c= color)
# plt.show()


# # VER EL PROMEDIO DE LAS 8 FILAS DE LA SEÑAL CONTINUA
# promedio = [ np.mean( i ) for i in senal_continua ]
# promedio1 = pd.Series( promedio )
# print( promedio1 )

# # HISTOGRAMA DEL PROMEDIO DEL PUNTO 1 
# sns.kdeplot( promedio )
# plt.show()

# # IMAGEN DE CALOR, tengo que pasar de 3 dimensiones a 2 
# # la señal tiene 176 epocas, dentro de cada una dde estas hay 2000 muestras
# # tengo que coger las 100 primeras muestras y las 100 ultimas de esas 176 epocas y crear una matruz de dos dimensiones
# # como lo hacemos ?
# new = senal[0, :100, :-100]
# sns.heatmap( new, cmap= "viridis" )
# plt.show()