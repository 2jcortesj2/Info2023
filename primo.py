#matriz = [ [0 for columna in range(5)] for fila in range(5) ]
matriz = []
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(0)
    matriz.append( fila )        

def verificarEspacio( matriz, fila, columna ):
    if matriz[fila][columna] == 0:
        return False # desocupado
    else:
        return True # ocupado
    
def asignarEspacio( matriz, fila, columna, nombre, id, serial ):
    if verificarEspacio( matriz, fila, columna ) == True:
        return "El espacio ya esta ocupado"
    else:
        matriz[fila][columna] = [ 1 , nombre, id, serial ]
        return matriz

def removerEspacio( matriz, serial ):
    for lista in matriz: # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        for i in lista:
            if i != 0 and i[3] == serial:
                posicion = lista.index( i )
                lista[posicion] = 0

while True:
    opcion = input( """
    MENU
    (1) Almacenar muestra 
    (2) Revisar muestra
    (3) Eliminar muestra
    (4) Ver espacios vacios
    (5) Salir
    >  """ )

    if opcion == '1': # ALMACENAR MUESTRA
        pass
    elif opcion == '2': # REVISAR MUESTRA
        pass
    elif opcion == '3': # ELIMINAR MUESTRA
        pass
    elif opcion == '4': # VER ESPACIOS VACIOS 
        pass
    elif opcion == '5': # SALIR
        pass

                
asignarEspacio( matriz, 2, 4, "andres", 2, 3 )
asignarEspacio( matriz, 2, 3, "josue", 1, 2 )
removerEspacio( matriz, 3 )
print( matriz )

