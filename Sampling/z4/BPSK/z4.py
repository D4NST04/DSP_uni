import matplotlib.pyplot as plt 
import numpy as np
from bitsToName import BTN 

imie = []
with open('bits.txt', 'r') as file:
    for i in file.readline():
        imie.append( int(i) )
print( 'Zakodowane imie w bitach' )
print( imie )

# Parametry
f_pr = int(16e3)
T = 0.1 
f_c = 30
bps = 1/T
t = len( imie ) / bps

# Modulowanie BPSK
wek_t_pr = np.linspace( 0, t, int(t*f_pr), False )
syg_pr = np.zeros( len(wek_t_pr) )

samps_per_bit = len( syg_pr ) // len( imie )

for bit in range( len(imie) ):
    if imie[bit] == 1: faza = 1
    else: faza = -1
    prz_pocz = bit*samps_per_bit
    prz_kon = (bit+1)*samps_per_bit
    czas = wek_t_pr[ prz_pocz : prz_kon ]
    sinus = faza * np.sin( 2*np.pi*f_c*czas )
    syg_pr[ prz_pocz : prz_kon ] = sinus

plt.plot( wek_t_pr, syg_pr )
plt.grid()
plt.show()

# Demodulowanie BPSK 
t_demod = wek_t_pr
syg_porownawczy = np.sin( 2*np.pi*f_c*t_demod )

mixed = syg_pr * syg_porownawczy

bity = []
for i in range( int(f_pr*T/2), len( mixed ), int(f_pr*T) ):
    if mixed[i] > 0: bity.append(1)
    else: bity.append(0)

#print( bity )
print( f'Czy udalo sie rozkodowac: {bity == imie}' )
print( f'Imie zakodowane to: {BTN( bity )}' )
