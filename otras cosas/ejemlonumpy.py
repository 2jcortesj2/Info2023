import numpy as np
import matplotlib.pyplot as plt

# Generar señal de ejemplo
eeg_signal = np.random.randn(100)
# print( eeg_signal )

# Calcular la transformada de Fourier
fft_signal = np.fft.fft(eeg_signal)
print( fft_signal )

# Calcular la frecuencia correspondiente a cada punto de la transformada
frequencies = np.fft.fftfreq(len(eeg_signal))

# Visualizar la transformada de Fourier
plt.plot( frequencies, np.abs(fft_signal) )
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.show()