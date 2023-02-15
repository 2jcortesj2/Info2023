class Person:
    
    def __init__( self ):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""

    ## SETTERS ##
    def setName( self, rol ):
        self.__nombre = input( f"Ingrese el nombre del {rol}: " )
    
    def setCedula( self, rol ):
        self.__cedula = input( f"Ingrese la cedula del {rol}: " )

    def setGenero( self, rol ):
        self.__genero = input( f"Ingrese el genero del {rol}: " )

    ## GETTERS ##
    def getName( self ):
        return print (self.__nombre)

    def getCedula( self ):
        return print (self.__cedula)

    def getGenero( self ):
        return print (self.__genero)
    

class Paciente( Person ):

    def __init__( self ):
        super().__init__() # hace alucion al constructor de la clase padre, sin embargo se puede poner o no 
        self.__servicio = ""

    def assignService( self ):
        self.__servicio = input( "Asignar servicio: " )
    
    def showService( self ):
        return print (self.__servicio)


class Empleado_Hospital( Person ):

    def __init__(self):
        super().__init__()
        self.__turno = ""

    def setTurn( self, turno ):
        self.__turno = turno

    def showTurn( self ):
        return print (self.__turno)


class Enfermera( Empleado_Hospital ):

    def __init__(self):
        super().__init__()
        self.__rango = ""

    def setRange( self, rango ):
        self.__rango = rango

    def showRange( self ):
        return print (self.__rango)


class Medico( Empleado_Hospital ):

    def __init__(self):
        super().__init__()
        self.__especialidad = ""

    def setSpeciality( self, especialidad ):
        self.__especialidad = especialidad
    
    def showSpeciality( self ):
        return print(self.__especialidad)
    

class Sistema( Person ):
    
    def __init__(self):
        self.__lista_pacientes = []
        
    def numeroDePacientes( self ):
        self.__numero_pacientes = len( self.__lista_pacientes )
        return self.__numero_pacientes
    
    def ingresarPaciente( self, rol ):
        i = '1'
        for i in range(1000):
            i = str(i)
            i = Paciente() 
            i.setName( rol )
            i.setGenero( rol )
            i.setCedula( rol )
            i.assignService()
            self.__lista_pacientes.append( i )
            print( self.numeroDePacientes() )
            i = i + '1'


"""
Un ejemplo para correr el codigo seria el siguienteñ
"""


paciente_1 = Sistema()
paciente_1.ingresarPaciente( "Paciente" )
