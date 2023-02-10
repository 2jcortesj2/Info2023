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
        return print (self.__nombre)

    def getCedula( self ):
        return print (self.__cedula)

    def getGenero( self ):
        return print (self.__genero)

################################################################################################################################

class Paciente( Person ):

    def __init__( self ):
        super().__init__() # hace alucion al constructor de la clase padre, sin embargo se puede poner o no 
        self.__servicio = ""

    def assignService( self, servicio ):
        self.__servicio = servicio
    
    def showService( self ):
        return print (self.__servicio)


################################################################################################################################

class Empleado_Hospital( Person ):

    def __init__(self):
        super().__init__()
        self.__turno = ""

    def setTurn( self, turno ):
        self.__turno = turno

    def showTurn( self ):
        return print (self.__turno)

################################################################################################################################

class Enfermera( Empleado_Hospital ):

    def __init__(self):
        super().__init__()
        self.__rango = ""

    def setRange( self, rango ):
        self.__rango = rango

    def showRange( self ):
        return print (self.__rango)

################################################################################################################################

class Medico( Empleado_Hospital ):

    def __init__(self):
        super().__init__()
        self.__especialidad = ""

    def setSpeciality( self, especialidad ):
        self.__especialidad = especialidad
    
    def showSpeciality( self ):
        return print(self.__especialidad)


p2 = Paciente()
p2.setName("Juan")
p2.getName()