import pymongo 
import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
# para trabajar con señales
import scipy.io as sio
import cv2
import seaborn as sns


class Sistema:

    def __init__( self, client ):
        my_data_base = client[ "Evaluacion_2" ]
        self.__senalData = my_data_base[ "señal" ]
        self.__senalContinua = []
        self.__senal = []
        self.__cedula = ''


    # METODOS PARA ASIGNAR LAS COSAS AL MONGO 
    def asignarNombre( self, nombre ): 
        c = { "Cedula": self.__cedula }
        d = { "$set": { "Nombre": nombre } }
        self.__senalData.update_one(c, d)

    def asignarCedula( self, cedula ): 
        self.__cedula = cedula
        c = { "Cedula": cedula }
        self.__senalData.insert_one(c)
        
    def asignarEdad( self, edad ): 
        c = { "Cedula": self.__cedula }
        d = { "$set": { "Edad": edad } }
        self.__senalData.update_one(c, d)

    def asignarsenal( self, nombreMat ):  
        ruta = r'' + nombreMat
        c = { "Cedula": self.__cedula }
        d = { "$set": { "Señal": ruta } }
        self.__senalData.update_one(c, d)
        cargar = sio.loadmat( ruta )
        self.__senal = cargar["data"]
        sensores = self.__senal.shape[0] 
        puntos = self.__senal.shape[1]
        epocas = self.__senal.shape[2]
        self.__senalContinua = np.reshape( self.__senal, ( sensores, puntos * epocas ), order= 'F' )

    def asignarImagenSenal( self, imagen ): 
        ruta = r'C:\Users\Josue Paniagua Lopez\OneDrive\Escritorio\Info2023\Info2023-3'
        c = { "Cedula": self.__cedula }
        d = { "$set": { "Imagen Señal": ruta + '\\' + imagen + '.png' } }
        self.__senalData.update_one(c, d) 

    def asignarMapaCalor( self, calor ): 
        ruta = r'C:\Users\Josue Paniagua Lopez\OneDrive\Escritorio\Info2023\Info2023-3'
        c = { "Cedula": self.__cedula }
        d = { "$set": { "Imagen calor": ruta + '\\' + calor + '.png' } }
        self.__senalData.update_one(c, d)


    # METODOS PARA IMPRIMIR POR CONSOLA
    def imprimirTamañoSeñal( self ):  
        cedula = self.__senalData.find_one( {"Cedula": self.__cedula} )
        ruta = cedula['Señal']
        cargar = sio.loadmat( ruta )
        senal = cargar["data"] 
        print( "La dimension es: ", senal.ndim )
        print( "Forma: ", senal.shape ) 

    def promedioFilasSeñalContinua( self ): 
        promedio = [ np.mean( i ) for i in self.__senalContinua ]
        promedio1 = pd.Series( promedio )
        return promedio1


    # METODOS PARA GRAFICAR
    def graficarSeñalContinua( self ): 
        plt.subplots(1)
        plt.plot(self.__senalContinua[0, 0:2500]) 
        plt.show()

    def graficarEpocaSeñal( self, sensor = 1, epoca = 1 ): 
        if 1 <= sensor <= self.__senal.shape[0] and 1 <= epoca <= self.__senal.shape[2]:
            new_signal = self.__senal[sensor-1, :, epoca-1]
            plt.plot( new_signal, color= 'purple' )
            plt.show()
        else:
            print( "El sensor o la epoca estan fuera del rango..." )

    def graficarSeñalColorDeterminado( self, color= 'k' ): 
        plt.subplots(1)
        plt.plot(self.__senal[0,:,0], c= color)
        plt.savefig("Señal color determinado.png")
        self.asignarImagenSenal("Señal color determinado")
        plt.show()
        
    def histogramaPromedioSeñal( self ): 
        sns.kdeplot( self.promedioFilasSeñalContinua() )
        plt.show()


    # METODOS PARA MOSTRAR IMAGENES
    def imagenCalor( self ):
        new = self.__senal[0, :100, :-100]
        sns.heatmap( new, cmap= "viridis" )
        plt.savefig("Imagen Calor.png")        
        self.asignarMapaCalor("Imagen Calor")
        plt.show()

    def imagenBlancoNegro( self ): # tambien hay que guardarla
        imagen = cv2.imread('Imagen Calor.png')
        imgGris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        cv2.imshow('Heatmap', imgGris)
        cv2.imwrite('ImagenCalorBlancoNegro.png', imgGris) 
        cv2.waitKey(0)

########################OTROS METODOS#################################################################

def validarInt( a ):
    try:
        a = int( a )
        return a
    except:
        return validarInt(input('Ingrese un numero valido: '))

######################################################################################################

def main():
    
    client = pymongo.MongoClient( "mongodb+srv://josuepaniagua:Ba5319466@cluster0.megrtoc.mongodb.net/?retryWrites=true&w=majority" )
    #db = client.test()

    cedula = input( "Ingrese el numero de la cedula: " )
    nombre = input( "Ingrese el nombre del paciente: " )
    edad = input( "Ingrese la edad del paciente: " )

    ruta = input( """
    INGRESE LA RUTA DEL ARCHIVO
    ruta :  """ )

    paciente = Sistema(client)

    paciente.asignarCedula(cedula)
    paciente.asignarNombre(nombre)
    paciente.asignarEdad(edad)
    paciente.asignarsenal(ruta)

    while True:

        opcion = input( """
        (1) Imprimir el tamaño de la señal
        (2) Graficar una señal de EEG continua
        (3) Graficar una epoca de una señal de EEG
        (4) Graficar la señal con un color determinado
        (5) Analisis de datos
        (6) Salir
        > """ )

        if opcion == '1':
            paciente.imprimirTamañoSeñal()

        elif opcion == '2':
            paciente.graficarSeñalContinua()

        elif opcion == '3':
            sensor = validarInt(input( "Sensor: " ))
            epoca = validarInt(input( "Epoca: " ))
            paciente.graficarEpocaSeñal( sensor, epoca ) 
        
        elif opcion == '4':
            color = input( 'Ingrese un color para el grafico: ' )
            try:
                paciente.graficarSeñalColorDeterminado( color ) 
            except:
                print( "El dato ingresado no es un color valido..." )

        elif opcion == '5':
            
            while True:
                opcion2 = input("""
                MENU 2.
                (1) Ver el promedio de las 8 filas de la señal continua
                (2) Ver el histograma del numeral anterior
                (3) Ver una imagen de calor 
                (4) Ver la imagen del numeral anterior a blanco y negro
                (5) Salir
                > """)
                
                if opcion2 == '1':
                    print(paciente.promedioFilasSeñalContinua())
                
                elif opcion2 == '2':
                    paciente.histogramaPromedioSeñal()
                
                elif opcion2 == '3':
                    paciente.imagenCalor()
                
                elif opcion2 == '4':
                    paciente.imagenBlancoNegro()
                
                elif opcion2 == '5':
                    break

        elif opcion == '6':
            break

        else:
            print('La opcion ingresada no es valida...')

if __name__ == '__main__':
    main()