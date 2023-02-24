import pymongo 

client = pymongo.MongoClient("mongodb+srv://josuepaniagua:Ba5319466@cluster0.megrtoc.mongodb.net/?retryWrites=true&w=majority")
db = client.test

my_date_base = client["Primera"]
my_collection = my_date_base["Clientes"]

my_dictionary = { "nombre": "camilo", "direccion": 0 } 

x = my_collection.insert_one( my_dictionary )

print( x.inserted_id ) # lo que hace el inserted_id es mostrarme como el objeto que agregue(Esas letras raras que)



### Para buscar en la base de datos se usa el find
"""
for i in my_collection.find( { "direccion": 0} ):
    print( i )
"""
#print( my_collection.find( { "direccion": 0 } ) )

# si quiero que me muestre todo en la base de datos 

for y in my_collection.find():
    print(y)
    my_collection.delete_one( y )
    print( y )


# ¿ que pasa si me equivoque asignando un valor?
my_query = { "nombre": "camilo", "direccion": 0 }
new_values = { "$set": { "nombre": "Luis" } }

my_collection.update_one( my_query, new_values )



## Para eliminar uno
#my_collection.delete_one( "Objeto que se quiere eliminar" )