import numpy as np
import matplotlib.pylab as plt

# Construya y[n]=sin (π*0.12n) en el intervalo 0 <= n <= 100.
x = np.arange(101)
y = np.sin( np.pi * 0.12 * x )

# Ahora vamos a graficar eso 
fig, ax = plt.subplots()
ax = plt.plot( x, y, label= "Con el sen" )

# Construya y2[n]=cos (2π*0.03n)
y1 = np.cos( 2 * np.pi * 0.03 * x )
ax = plt.plot( x, y1, label= "Con el cos" )

y3 = y + y1
y4 = y * y1
ax = plt.plot( x, y3, label= "Suma",  )
ax = plt.plot( x, y4, label= "multiplicaion" )
plt.legend()
plt.show()


