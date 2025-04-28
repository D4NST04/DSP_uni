import matplotlib.pyplot as plt
import numpy as np

# Parametry
t = 1
amp = 1
fb = 50

samp = [ int( 1e4 ),
        51,
        50,
        49,
        int( 1e4 ),
        26,
        25,
        24 ]
colors = [ 'red', 'blue', 'green', 'black' ] 
num_of_checks = 2 
per_check = 4
#=====================================#

for n in range( num_of_checks ):
    for i in range( per_check ):
        which = n*4 + i
        wek_t = np.linspace( 0, t, int( t*samp[which] ), False )
        sig = amp * np.sin( 2*np.pi*fb*wek_t )
        plt.plot( wek_t, sig, color=colors[i],
                 label=f'{samp[which]} Hz' )
    plt.legend()
    plt.show()
