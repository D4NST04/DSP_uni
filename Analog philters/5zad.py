import numpy as np 
from matplotlib import pyplot as plt 
from scipy import signal as sig 

# Dane
# Przedzial [ 90; 102 ) MHz
f = np.linspace( int(90e6), int(102e6), 1200, endpoint=False )
f0 = int(96e6) # Czestotliwosc srodkowa
w = 2*np.pi*f
# Zafalowania w przepustowym <= 3dB
Rp = 3
# Tlumienie w zaporowym > 40dB
Rs = 40 

# Testowy filtr 96 +- 1 MHz 
N = 5
w1 = 2*np.pi * ( f0 - 1e6 )
w2 = 2*np.pi * ( f0 + 1e6 )

bm, an = sig.ellip( N, Rp, Rs, [ w1, w2 ], btype='bandpass', analog=True )
Y_jw = np.polyval( bm, 1j*w )
X_jw = np.polyval( an, 1j*w )
H_test = Y_jw / X_jw
H_test = H_test / np.max( np.abs( H_test ) )
H_test_dB = 20 * np.log10( np.abs( H_test ) ) 

plt.figure( 'Filtr testowy' )
plt.plot( f, H_test_dB )
plt.xlim( 92e6, 100e6 )
plt.grid( True )
plt.show()

# Filtr docelowy
N = 3
w1 = 2*np.pi * ( f0 - 1e5 )
w2 = 2*np.pi * ( f0 + 1e5 )

bm, an = sig.ellip( N, Rp, Rs, [ w1, w2 ], btype='bandpass', analog=True )
Y_jw = np.polyval( bm, 1j*w )
X_jw = np.polyval( an, 1j*w )
H_doc = Y_jw / X_jw
H_doc = H_doc / np.max( np.abs( H_doc ) )
H_doc_dB = 20 * np.log10( np.abs( H_doc ) ) 

plt.figure( 'Filtr docelowy' )
plt.plot( f, H_doc_dB )
plt.xlim( 92e6, 100e6 )
plt.grid( True )
plt.show()

# Porownanie filtrow
plt.figure( 'Porownanie filtrow' )
plt.plot( f, H_test_dB, 'b', label='Testowy' )
plt.plot( f, H_doc_dB, 'r', label='Docelowy' )
plt.xlim( 92e6, 100e6 )
plt.legend()
plt.grid( True )
plt.show()

# Porownanie i zaznaczenie waznych rzeczy
plt.figure( 'Porownanie filtrow' )
plt.plot( f, H_test_dB, 'b', label='Testowy' )
plt.plot( f, H_doc_dB, 'r', label='Docelowy' )
plt.plot( [ 95.9e6, 95.9e6 ], [ -100, 10 ], 'k-' )
plt.plot( [ 96.1e6, 96.1e6 ], [ -100, 10 ], 'k-' )
plt.plot( [ 95e6, 95e6 ], [ -100, 10 ], 'k-' )
plt.plot( [ 97e6, 97e6 ], [ -100, 10 ], 'k-' )
plt.plot( [ 92e6, 100e6 ], [ -3, -3 ], 'k-' )
plt.plot( [ 92e6, 100e6 ], [ -40, -40 ], 'k-' )
plt.xlim( 92e6, 100e6 )
plt.ylim( -99, 2 )
plt.legend()
plt.grid( True )
plt.show()
