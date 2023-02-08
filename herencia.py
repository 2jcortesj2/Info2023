
class Ave:

    def __init__(self, tipo, vuela):
        self.ave = tipo
        self.vuelo = vuela
        self.oviparos = True
        self.pico = True

    # acciones basicas 
    def comer( self, comida ):
        print( "Este tipo de ave come normalmente " + comida )

    def volar( self ):
        print( "Este tipo de ave puede volar: " + self.vuelo )


class Ganso( Ave ):

    def __init__( self, tipo, vuela, accion, pata ):
        super().__init__( tipo, vuela )
        self.habilidad = accion
        self.patas = pata

    def destreza(self):
        print( "Esta ave se puede: " + self.habilidad )
    
class Pato( Ave ):
    pass

class Gallina( Ave ):
    pass


ave_1 = Ganso( "carnivoro", True, "vuela", 2 )
ave_1.comer( "carne" )