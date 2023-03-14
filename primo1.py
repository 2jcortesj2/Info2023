# SISTEMA DE MUESTRAS DE LABORATORIO DE LA FACULTAD DE INGENIERÍA
#crear una lista vacía  
matriz = []
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(1)
    matriz.append( fila )  

fila = 0
columna = 0
#crear un ciclo infinito
while True:
  #crear un menú con las opciones
  menu = int(input('''\nIngrese la opción que desea realizar:
1. Almacenar muestra.
2. Revisar muestra. 
3. Eliminar muestra. 
4. Ver espacios vacios. 
5. Salir. 
-> '''))

    
  #condicionales segun las opciones
  if menu==1:
    print("\nUsted ha ingresado 1: Almacenar muestra.")
    print("\nA continuación ingrese la información necesaria")

    #pedir informacion: estudiante,id, serial de la muestra, hora de ingreso.

    nom = input("\nIngrese el nombre del estudiante: ")
    id = int( input('\nDigite el número de docuemnto: ') )
    serial = int( input("\nDigite el serial de la muestra: ") )
    hora = input('\nDigite la hora de ingreso de la muestra: ')
    time = input('\nDigite el tiempo que la muestra estará almanecada: ')
    
    fila = int( input( "\nIngrese la fila en un rango de 5: " ) ) - 1
    columna = int( input( "\nIngrese la columna en un rango de 5: " ) ) - 1
    if matriz[fila][columna] != 1:
       print( "Ese lugar ya esta ocupado..." )
       continue
    matriz[fila][columna] = [ nom, id, serial, hora, time ]
       
    print("\nLa muestra fue almacenada con éxito")
    print(matriz)

  elif menu == 2:
    print("\nHa ingresado 2: Revisar muestra.")
    serialmuestra = int( input("\nPor favor digite el serial de la muestra: " ) )

    for lista in matriz:
       for i in lista:
          if i != 1 and i[2] == serialmuestra:
             print( f"""
             INFORMACION CONTENIDA DE LA MUESTRA
             Nombre: {i[0]}
             Cedula: {i[1]}
             Serial de la muestra: {i[2]} 
             Hora de ingreso de la muestra: {i[3]} 
             Tiempo de almacenamiento: {i[4]}              
             """ )

  elif menu == 3: 
    #eliminar muestra
    print('\nUsted ha ingresado 3: Eliminar muestra.')
    serialmuestra=int(input("\nPor favor digite el serial de la muestra que desea eliminar: "))

      
    for lista in matriz: # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        for i in lista:
            if i != 1 and i[2] == serialmuestra:
                posicion = lista.index( i )
                lista[posicion] = 1
                print( "informacion eliminada..." )
                print( matriz )
                print( matriz.index( lista ) )
                
  elif menu==4:
    #espacios=[]
    #for i in range(len(matriz)):
      #for j in range(len(matriz):
        #if i != j:
          #if matriz[i]==numeros[j]:
            #espacios.append(matriz(i))
    #print("hay disponibles ")
    pass
    #ver espacios vacios
    
  
  elif menu==5:
    print('\nUsted ha ingresado 5: Salir.')
    salirmenu=int(input('''
    ¿Está seguro que desea salir?: 
    1. Sí.
    2. No.
    -> '''))
    if salirmenu==1:
        print('''
    Que tenga un buen día.
    Hasta la próxima.
      ''')
        break
    else:
        continue

  

  
  
  else:
    print("\nPor favor ingrese una opción válida")