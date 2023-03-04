import pymongo

client = pymongo.MongoClient( "mongodb+srv://josuepaniagua:Ba5319466@cluster0.megrtoc.mongodb.net/?retryWrites=true&w=majority" )
bd = client.test

my_data_base = client[ "Ejemplo" ]
my_first_collection = my_data_base[ "gatas" ]

nombre = "samuel"
dosis = 0


primera = { "nombre": nombre, "Dosis": dosis  } 
segunda = { "nombre": "carlos", "Dosis": 2 }
x = my_first_collection.insert_one( primera )
y = my_first_collection.insert_one( segunda )
print("ciao")

lista = list(my_first_collection.find( {"nombre": "carlos"} )) 
print( lista[2] )

def main():

    client = pymongo.MongoClient( "" )
