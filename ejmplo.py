
class Perro:

    def __init__(self, nombre, color, raza, peludo):
        self.nombre = nombre
        self.color = color
        self.race = raza
        self.peludo = peludo

    def comiendo( self ):
        print( f"{self.nombre} esta comiendo" )

    def Race( self ):
        print( f"{self.nombre} es de la raza: {self.race} y {self.peludo} es peludo" )

mi_perro = Perro( "Samuel", "negro", "Pastor aleman", "Si" )
mi_perro.comiendo()
mi_perro.Race()

