import pymongo 

client = pymongo.MongoClient("mongodb+srv://josuepaniagua:Ba5319466@cluster0.megrtoc.mongodb.net/?retryWrites=true&w=majority")
db = client.test

my_date_base = client["hbdd"]
my_collection = my_date_base["Clientes"]

my_dictionary = { "nombre": "juan", "direccion": 0 } 

x = my_collection.insert_one( my_dictionary )

print( x.inserted_id ) # lo que hace el inserted_id es mostrarme como el objeto que agregue(Esas letras raras que)



### Para buscar en la base de datos se usa el find
for x in my_collection.find( { "direccion": 0} ):
    print( x )



# si quiero que me muestre todo en la base de datos 
for y in my_collection.find():
    print(y)



## Para eliminar uno
my_collection.delete_one(  )



# ¿ que pasa si me equivoque asignando un valor?
myquery = { "nombre": "camilo", "direccion": 0 }
new_values = { "$set": { "nombre": "Luis" } }

my_collection.update_one( myquery, new_values )
