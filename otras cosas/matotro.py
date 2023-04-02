import matplotlib.pyplot as plt
import numpy as np

x = np.linspace( 0, 2 * np.pi, 4000 )
y = np.sin( x )
y1 = np.cos( x )

fig, ax = plt.subplots( 1, 2 , sharex= True, sharey= True)
ax[0].plot(x, y, label= 'Seno')
ax[1].plot(x, y1, label= 'Coseno')
ax[0].legend()
ax[1].legend()
plt.show()