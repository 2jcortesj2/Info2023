
class Sustancia:

    def __init__( self ):
        self.__identificador = None
        self.__ubicacion = None
        self.__acceso = None
        self.__peligrosa = None

    # METODOS PARA ASIGNAR
    def sustanciaAsignarIdentificador( self, identificador ):
        self.__identificador = identificador

    def sustanciaAsignarUbicacion( self, fila, columna ):
        self.__ubicacion = list( fila, columna )

    def sustanciaAsignarAcceso( self, acceso ): # Acceso a estudiantes
        self.__acceso = acceso

    def sustanciaAsignarPeligrosa( self, peligrosa ):
        self.__peligrosa = peligrosa

    # METODOS PARA VER
    def sustanciaVerIdentificador( self ):
        return self.__identificador
    
    def sustanciaVerUbicacion( self ):
        return self.__ubicacion
    
    def sustanciaVerAcceso( self ):
        return self.__acceso 

    def sustanciaVerPeligrosa( self ):
        return self.__peligrosa 

class AcidoBase:
    def __init__(self):
        self.__concentracion = None
        self.__efectos = None

    def acidoBaseConcentracion( self, concentracion ):
        self.__concentracion = concentracion
    
    def acidoBaseVerConcentracion( self ):
        return self.__concentracion
        

class Alcohol:
    pass

class Solvente:
    pass

class Otro:
    pass


class Sistema:
    pass





