import matplotlib.pyplot as plt 
import numpy as np
from scipy.signal import welch 

# Parametry
fs = int( 1e4 )         # Czestotliwosc pseudo-analogowa
fn = 50                 # Czestotliwosc nosna
fm = 1                  # Czestotliwosc modulujaca
d = 5                   # Glebokosc modulacji
t = 1                   # Czas sygnalu
f_samp = 25             # Czestotliwosc probkowania

# 1 czesc 
wek_t_anal = np.linspace( 0, t, t*fs, False )

phi = 2 * np.pi * d * np.sin(2 * np.pi * fm * wek_t_anal )
sygnal_anal = np.sin(2 * np.pi * fn * wek_t_anal + phi)

plt.plot( wek_t_anal, sygnal_anal, color='red',
         label='Sygnal zmodulowany')
plt.plot( wek_t_anal, phi, color='blue',
         label='Sygnal modulujacy' )
#plt.plot( wek_t_anal, f_chwilowa )
plt.legend()
plt.show()


# 2 czesc 
wek_t_samp = np.linspace( 0, t, t*f_samp, False )

phi = 2 * np.pi * d * np.sin(2 * np.pi * fm * wek_t_samp )
sygnal_samp = np.sin(2 * np.pi * fn * wek_t_samp + phi)
plt.plot( wek_t_anal, sygnal_anal, color='red',
         label='Sygnal pseudo-analogowy')
plt.plot( wek_t_samp, sygnal_samp, color='blue',
         label='Sygnal probkowany' )
#plt.plot( wek_t_anal, f_chwilowa )
plt.legend()
plt.show()

# 3 czesc
plot_freq_1, psd_1 = welch(sygnal_anal, fs, nperseg=25)
plot_freq_2, psd_2 = welch(sygnal_samp, f_samp, nperseg=25)

plt.semilogy( plot_freq_1, psd_1, color='red', 
             label='Gestosc mocy syg pseudo-analogowego' )
plt.semilogy( plot_freq_2, psd_2, color='blue',
             label='Gestosc mocy syg probkowanego' )
plt.legend()
plt.show()
