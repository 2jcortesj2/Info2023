import matplotlib.pyplot as plt
import numpy as np

x = np.linspace( 0, 2*np.pi, 200 ) # linspace( valor_inicial, valor_final, numero de valores )
y = np.sin( x )

fig, ax = plt.subplots()
ax.plot(x, y)

# otro ejemplo 
# fig = plt.figure()
fig, ax = plt.subplots()
#plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
ax.plot([1, 2, 3, 4], [1, 4, 2, 3]) # para definir los puntos de la grafica
ax.grid() # para que quede con los cuadros divididos
#plt.show()


np.random.seed( 19680801 )
data = {'a' : np.arange(50),
        'c' : np.random.randint(0, 50, 50),
        'd' : np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots( figsize= (5, 2.7), layout= 'constrained' )
ax.scatter('a', 'b', c= 'c', s= 'd', data = data)
ax.plot(data['a'], label= "a", c= "#1AEA8F")
# ax.scatter(data['a'], data['b'],c='k')
ax.set_xlabel( 'entry a' )
ax.set_ylabel( 'entry b' )
ax.legend()
plt.show()
