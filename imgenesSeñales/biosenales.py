# %%
#PRIMER PUNTO

#libreria de entrada salida de datos
import scipy.io as sio
#transforamda rapida de fourier, para cuantificar las oscilaciones
import scipy.fftpack as fft
#manejo de tensores ndarray
import numpy as np  
#graficar
import matplotlib.pyplot as plt

#estoy cargando unos datos que fueron previamente recolectados
#usamos el sio para cargar los datos
path = r'C:\Users\Josue Paniagua Lopez\OneDrive\Escritorio\Info2023\Info2023-3\imgenesSeñales\C001R_EP_reposo.mat'
mat_contents = sio.loadmat(path) 
# print('La variable cargada es del tipo: ' + str(type(mat_contents))) 
# print('las llaves son: ' + str(mat_contents.keys())) 

senal = mat_contents['data'] 
# print("dimensión: ",senal.ndim) 
# print("Forma: ",senal.shape) 

#COMO HACEMOS CONTINUA
sensores = senal.shape[0] 
print( sensores )
puntos = senal.shape[1] 
print( puntos )
epocas = senal.shape[2] 
print( epocas )

#reshape(senal_original, forma_nueva)
# print( senal.shape  )
senal_continua = np.reshape(senal,(sensores,puntos*epocas),order = 'F') 
# print( senal_continua )
# print(senal_continua.shape) 

#graficamos
plt.subplot(1,2,1) 
plt.plot(senal[0,:,0]) 

plt.subplot(1,2,2) 
plt.plot(senal_continua[0,0:2200]) 


plt.show() 