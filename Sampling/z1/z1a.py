import matplotlib.pyplot as plt 
import numpy as np 

# Parametry
t = 0.1
amp = 230
fb = 50
samp = [ int( 1e4 ), 
        500, 
        200 ]
colors = [ 'red', 'green', 'blue' ]
#=====================================#

for i in range( 3 ):
    wek_t = np.linspace( 0, t, int( t*samp[i] ), False )
    sig = amp * np.sin( np.pi*2*fb*wek_t )
    plt.plot( wek_t, sig, color=colors[i],
             label=f'{samp[i]} Hz')

plt.legend()
plt.show()
