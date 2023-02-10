# Para hacer atributos provados

class Ejemplo:

    def __init__( self ):
        self.__nombre = "Josue"
        self.__apellido = "Paniagua"
        self.__edad = "19"

    def getNombre( self ):
        print( f"Tu nombre es: {self.__nombre}, tu apellido es: {self.__apellido}, tu edad es: {self.__edad}" )

    def __Apellido( self ):
        print( self.__apellido )

    def getApellido( self ):
        return self.__Apellido()

persona_1 = Ejemplo()
persona_1.getNombre()
persona_1.getApellido()

