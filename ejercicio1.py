class Person:
    
    def __init__( self ):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""

    ## SETTERS ##
    def setName( self, nombre ):
        self.__nombre = nombre
    
    def setCedula( self, cedula ):
        self.__cedula = cedula

    def setGenero( self, genero ):
        self.__genero = genero

    ## GETTERS ##
    def getName( self ):
        return self.__nombre

    def getCedula( self ):
        return self.__cedula

    def getGenero( self ):
        return self.__genero

################################################################################################################################

class Paciente( Person ):

    def __init__( self ):
        super().__init__() # hace alucion al constructor de la clase padre, sin embargo se puede poner o no 
        self.__servicio = ""

    def assignService( self, servicio ):
        self.__servicio = servicio
    
    def showService( self ):
        return self.__servicio


################################################################################################################################


