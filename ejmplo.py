
class Perro:

    def __init__(self, nombre, color, raza, peludo):
        self.nombre = nombre
        self.color = color
        self.raza = raza
        self.peludo = peludo

    def comiendo( self, nombre ):
        print( f"{nombre} esta comiendo" )

    def raza( self, nombre, raza, peludo ):
        print( f"{nombre} es de la raza: {raza} y es {peludo}" )