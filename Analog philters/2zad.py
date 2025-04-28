import numpy as np 
from matplotlib import pyplot as plt
import scipy.signal as sig 


N = [ 2, 4, 6, 8 ]
w3dB = 200*np.pi
kolorki = [ 'r', 'g', 'b', 'c', 'm', 'y', 'k' ]

bieguny = []
fazy = []
transmitancje = []

w = np.linspace( 0, int( 1e4 ), 1000, endpoint=False )
s = 1j * 2 * np.pi * w 

R = 2*np.pi*w3dB
alpha = np.linspace( 0, 2*np.pi, 1000, endpoint=False )
c = R * np.cos( alpha )
s = R * np.sin( alpha )

for n in N:
    # Liczenie biegunow
    dPhi = np.pi / n 
    phi = dPhi * np.linspace( 0, n, n, endpoint=False )\
            + np.pi/2 + dPhi/2
    p = R * np.exp( 1j*phi )
    bieguny.append( p )

    wzm = np.prod( -1*p )
    an = np.poly( p ).real
    X_w = np.polyval( an, 2j*np.pi*w )

    H = wzm / X_w
    transmitancje.append( H )
    
    faza = np.angle( H )
    fazy.append( faza )

    # Do Odpowiedzi
    if n == 4:
        sys = sig.TransferFunction( np.array([1]), an )

        t1, y1 = sig.impulse( sys )
        t2, y2 = sig.step( sys )

# Wykresy                    
for i in range( len( bieguny ) ):
    plt.subplot( 2, 2, i+1 )
    plt.title( f'Bieguny N={2+2*i}' )
    plt.plot( np.real( bieguny[i] ), np.imag( bieguny[i] ), 'ro' )
    plt.plot( c, s, 'k-' )
    plt.grid()
    plt.axis( 'square' )
plt.show()

plt.title( '|H(w)| liniowe' )
for i in range( len( transmitancje ) ):
    plt.plot( w, np.abs(transmitancje[i]), 
             color=f'{kolorki[i]}',
             label=f'N={N[i]}')
plt.grid()
plt.legend( loc='upper left' )
plt.show()

plt.title( '|H(w)| logarytmiczne' )
for i in range( len( transmitancje ) ):
    H_lg = 20 * np.log10( np.abs( transmitancje[i] ) )
    plt.semilogx( w, H_lg, 
             color=f'{kolorki[i]}',
             label=f'N={N[i]}')
plt.grid()
plt.legend( loc='upper left' )
plt.show()

plt.title( 'Cha-ka fazowa' )
for i in range( len( transmitancje ) ):
    plt.plot( w, fazy[i], 
             color=f'{kolorki[i]}',
             label=f'N={N[i]}')
plt.grid()
plt.legend( loc='upper left' )
plt.xlim( 0, 2000 )
plt.show()

# Odpowiedzi
plt.figure( 'Odp impuls' )
plt.plot( t1, y1 )
plt.grid( True )

plt.figure( 'Odp skok' )
plt.plot( t2, y2 )
plt.grid( True )

plt.show()
