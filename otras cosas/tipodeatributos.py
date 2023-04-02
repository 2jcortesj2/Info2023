class Cosa:

    def __init__( self, publico:str = "publico", protegido:str = "Protegido", privado:str = "privado" ):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado

    def informacion( self ):
        print(
            (
                f"Publico: {self.publico}"
                f"Protegido: {self._protegido}"
                f"Privado: {self.__privado}"
            )
        )

cosa_1 = Cosa()
print( cosa_1.publico )
#print( cosa_1.__privado )
print( cosa_1._protegido )
