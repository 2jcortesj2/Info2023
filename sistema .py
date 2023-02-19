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
        return self.__nombre

    def getCedula( self ):
        return self.__cedula

    def getGenero( self ):
        return self.__genero
    
    def guardarInfo( self ):
        return self.__nombre, self.__cedula, self.__genero


class Paciente( Person ):

    def __init__( self ):
        super().__init__() # hace alucion al constructor de la clase padre, sin embargo se puede poner o no 
        self.__servicio = ""

    def assignService( self ):
        self.__servicio = input( "Asignar servicio: " )
    
    def showService( self ):
        return self.__servicio


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
        self.__lista_nombre = []
        self.__lista_cedula = []
        self.__lista_genero = []
        self.__lista_servicio = []
        self.__diccionario_pacientes = {}

    def numeroDePacientes( self ):
        self.__numero_pacientes = len( self.__lista_pacientes )
        return print( self.__numero_pacientes )
    
    def ingresarPaciente( self, rol ):
        p = Paciente() 
        p.setName( rol )
        p.setGenero( rol )
        p.setCedula( rol )
        p.assignService()
        self.__lista_pacientes.append( p.guardarInfo() )
        self.__lista_nombre.append( p.getName() )
        self.__lista_cedula.append( p.getCedula() )
        self.__lista_genero.append( p.getGenero() )
        self.__lista_servicio.append( p.showService() )
        self.__diccionario_pacientes.update( {'Nombre' : self.__lista_nombre, 'Cedula' : self.__lista_cedula, 'Genero' : self.__lista_genero, 'Servicio' : self.__lista_servicio} )
        print( self.__diccionario_pacientes )
        #print( self.__lista_pacientes )
        #print( self.numeroDePacientes() )

    def verDatosPacientesLista( self ):
        cedula = input( 'Ingrese la cedula del paciente que quiere buscar en la lista: ' )
        for c in self.__lista_pacientes:
            if cedula == c[1]:
                return print(c)

    def verDatosPacientesDiccionario( self ):
        cedula = input( "Ingresar la cedula del pacientes que busca en el diccionario: " )
        for p, c in enumerate( self.__diccionario_pacientes['Cedula'] ):  # ENUMERATE
            if cedula == c:
                print( 
                    f"""
                    Nombre: { self.__diccionario_pacientes['Nombre'][p] }, 
                    cedula : {self.__diccionario_pacientes['Cedula'][p]}, 
                    Genero: {self.__diccionario_pacientes['Genero'][p]}
                    Servicio: {self.__diccionario_pacientes['Servivio'][p]}"""
                    )
            else:
                print( "No hay ningun paciente que coincida con esa cedula" )
                
    def modificarGenero( self ):
        cedula = input( "Ingrese la cedula de la persona que desea modificar el genero: " )
        for p, id in enumerate(self.__diccionario_pacientes['Cedula']):
            if cedula == id:
                self.__diccionario_pacientes['Genero'][p] = input( "Ingrese el nuevo genero del paciente: " )

    def modificarCedula( self ):
        cedula = input( "Ingrese la cedula que introdujo anteriormente por error: " )
        for p, id in enumerate(self.__diccionario_pacientes['Cedula']):
            if cedula == id:
                self.__diccionario_pacientes['Cedula'][p] = input( "Ingrese la nueva cedula del paciente: " )

    def modificarNombre( self ):
        cedula = input( "Ingrese la cedula de la persona que desea modificar el nombre: " )
        for p, id in enumerate(self.__diccionario_pacientes['Cedula']):
            if cedula == id:
                self.__diccionario_pacientes['Nombre'][p] = input( "Ingrese el nombre del paciente: " )
        
    def eliminarPaciente( self ):
        cedula = input( "Ingrese la cedula del paciente que desea eliminar: " )
        for p, id in enumerate( self.__diccionario_pacientes['Cedula'] ):
            if cedula == id:
                del self.__diccionario_pacientes['Cedula'][p]
                del self.__diccionario_pacientes['Genero'][p]
                del self.__diccionario_pacientes['Nombre'][p]
                del self.__diccionario_pacientes['Servicio'][p]
                print( "Paciente eliminado con exito" )


################# Funcion enumerate con el for ##############

######################## FUNCIO MAIN ########################


def main():

    p = Sistema()

    while True:
        opcion = int( input( """
        1- Ingresar paciente
        2- Ver datos del paciente
        3- Ver el numero de pacientes
        4- Modificar genero de un paciente
        5- Modificar cedula de un paciente
        6- Modificar nombre de un paciente
        7- Eliminar paciente
        8- Salir
        > """ ) )

        if opcion == 1:
            p.ingresarPaciente( "Paciente" )
        elif opcion == 2:
            p.verDatosPacientesDiccionario()
        elif opcion == 3:
            p.numeroDePacientes()
        elif opcion == 4:
            p.modificarGenero()
        elif opcion == 5:
            p.modificarCedula()
        elif opcion == 6:
            p.modificarNombre()
        elif opcion == 7:
            p.eliminarPaciente()
        elif opcion == 8:
            break

if __name__ == '__main__': # ya viene definido asi para que ccorra el sistema
    main()