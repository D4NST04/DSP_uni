import matplotlib.pyplot as plt 
import numpy as np 

imie = []
with open( 'bits.txt', 'r' ) as file:
    content = file.readlines()[0]
    for i in range( 0, len(content), 2 ):
        inPhase = int( content[i] )
        quadrature = int( content[i+1] )
        imie.append( [ inPhase, quadrature ] )
    print( 'Zakodowane imie w parach bitow: ' )
    print( imie )

def pairToPhase( para ):
    # 00 -> 1ćw 
    # 01 -> 2ćw
    # 10 -> 3ćw
    # 11 -> 4ćw
    phase = 0.25
    if para[1] == 1: phase += 0.5
    if para[0] == 1: phase += 1
    

    return ( phase * np.pi )

def phaseToPair( phase ):
    phase = np.mod( phase, 2*np.pi )

    if 0 <= phase < np.pi/2: return [0,0]
    elif np.pi/2 <= phase < np.pi: return [1,0]
    elif np.pi <= phase < 3*np.pi/2: return [1,1]
    else: return [0,1]

# Parametry
f_pr = int( 16e3 )
T = 0.1
f_c = 30
symPerSec = 1/T 
t = len(imie) / symPerSec

# Modulowanie QPSK
wek_t = np.linspace( 0, t, int(f_pr*t), False )
syg_pr = np.zeros( len(wek_t) )

smpPerPair = len( syg_pr ) // len( imie )

for pair in range( len(imie) ):
    phi = pairToPhase( imie[pair] )
    prz_pocz = pair*smpPerPair
    prz_kon = (pair+1)*smpPerPair
    czas = wek_t[ prz_pocz : prz_kon ]
    sinus = np.sin( 2*np.pi*f_c*czas + phi )
    syg_pr[ prz_pocz : prz_kon ] = sinus 

plt.plot( wek_t, syg_pr )
plt.grid()
plt.show()
"""
recovered = []
for pair in range( len(imie) ):
    prz_pocz = pair*smpPerPair
    prz_kon = (pair+1)*smpPerPair
    czas = wek_t[ prz_pocz : prz_kon ]
    symSyg = syg_pr[ prz_pocz : prz_pocz ]
    print(f"pair: {pair}, prz_pocz: {prz_pocz}, prz_kon: {prz_kon}, len(symSyg): {len(symSyg)}")
    I = np.mean(symSyg * np.cos(2 * np.pi * f_c * czas))
    Q = np.mean(symSyg * np.sin(2 * np.pi * f_c * czas))
    phase = np.arctan2(Q, I)

    recovered.extend( phaseToPair( phase ) )

print( recovered )
"""

