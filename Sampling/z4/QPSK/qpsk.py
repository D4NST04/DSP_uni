import matplotlib.pyplot as plt 
import numpy as np 

# Parametry
f_pr = int( 16e3 )
T = 0.1
fc = 30

bps = 1/T

imie = ""
with open( 'bits.txt', 'r' ) as file:
    content = file.readlines()[0]
    for i in range( 0, len(content), 2 ):
        inPhase = int( content[i] )
        quadrature = int( content[i+1] )
        imie += ( str(inPhase) + str(quadrature) )
    print( 'Zakodowane imie w parach bitow: ' )
    print( imie )

pairToSym = {
    '00':  1+1j,   # 45st
    '01':  1-1j,   # 315st
    '10': -1+1j,   # 135st
    '11': -1-1j    # 225st
    }



symbole = [imie[i:i+2] for i in range( 0, len(imie), 2 ) ]
qpsk_sym = np.array( [pairToSym[b] for b in symbole] )

t = np.linspace( 0, T, int(f_pr*T), endpoint=False )
sygnal = []
for sym in qpsk_sym:
    i_wav = np.real(sym) * np.cos( 2*np.pi*f_pr*t )
    q_wav = np.imag(sym) * np.sin( 2*np.pi*f_pr*t )
    sygnal.extend( i_wav - q_wav )

sygnal = np.array( sygnal )

plt.plot( np.imag(sygnal) )
plt.grid()
plt.show()
