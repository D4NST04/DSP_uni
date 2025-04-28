import matplotlib.pyplot as plt 
import numpy as np 
from scipy.io import loadmat
from scipy.signal import correlate
from myCorr import corr

# Parametry
K = 4
M = 32
N = 512

sygnal = loadmat( 'adsl_x.mat', simplify_cells=True )

x = sygnal["x"].flatten()

print( "Długość sygnału: ", len(x) )
print( "Oczekiwana długość: ", K*(M+N) )

# Na najwieksze wartości korelacji
najwieksze = []

# Możliwe pozycje prefiksu
for i in range( len(x)-M-N ):
    prefix = x[ i : i+M ]
    koniec = x[ i+N : i+N+M ]
    
    # corr to moja funkcja
    wynik = corr(prefix, koniec )
    # correlate to funkcja pythona
#    wynik = correlate(prefix, koniec, mode="valid")

    max_corr = np.max( wynik )
    najwieksze.append( max_corr )

plt.plot( najwieksze )
plt.title( "Wykres korelacji prefiksów" )
plt.show()

print( "Pierwszy prefiks zaczyna się w: ", end="" )
print( najwieksze.index( np.max( najwieksze ) ), "próbce." )
