import matplotlib.pyplot as plt 
import numpy as np 

# Parametry
fs = 100
t = 1
f_step = 5
f_min = 0
f_max = 300
wave = 1        # 1 sinus, 0 cosinus

interesujace = [ 5,     105,    205 ]
# interesujace = [ 95,    195,    295 ]
# interesujace = [ 95,    105         ]

samp_count = 1 + (f_max-f_min)//f_step 
f_wav = np.linspace( f_min, f_max, samp_count, True )
wek_t = np.linspace( 0, t, t*fs, False )

wyniki = []

for i in range( samp_count ):
    arg = 2*np.pi*f_wav[ i ]*wek_t
    if wave == 1:
        wynik = np.sin( arg )
    else:
        wynik = np.cos( arg )
    wyniki.append( wynik )

    plt.subplot( 5, 5, i%25+1 )
    plt.plot( wek_t, wynik )
    plt.title( f'({i+1}): {f_wav[i]}Hz' )

    if i%25 == 24 or i==samp_count-1:
        plt.show()
        plt.close()

ile_int = len( interesujace )


for i in range( ile_int ):
    plt.subplot( ile_int, 1, i+1 )
    index = interesujace[i] // 5
    plt.plot( wek_t, wyniki[index] )
    plt.title( f'{interesujace[i]}Hz' )

plt.show()
    
