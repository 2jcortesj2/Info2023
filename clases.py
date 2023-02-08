# el metodo __str__

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)
print(p1.name)
print(p1.age)

# se puede cambiar la edad y asi mismo las variables
p1.age = 58
print(p1.age)

# para eliminar objetos se hace 
del p1

