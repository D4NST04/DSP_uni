import numpy as np 
from matplotlib import pyplot as plt 
from scipy import signal as sig 

# Parametry
f_s = 256e3
f0 = f_s/2 
f3dB = f0/2 
w0 = 2*np.pi*f0
w3dB = 2*np.pi*f3dB
sig.cheby1
f = np.linspace( 0, int(3e5), int(3e5), endpoint=False )
w = 2 * np.pi * f


# Butterworth --------------------------------------------
def butterDlaN( N ):
    bn, an = sig.butter( N, w3dB, analog=True )
    Y_jw = np.polyval( bn, 1j*w )
    X_jw = np.polyval( an, 1j*w )
    H_Butter = Y_jw / X_jw
    H_Butter = H_Butter / np.max( np.abs( H_Butter ) )
    H_Butter_dB = 20 * np.log10( np.abs( H_Butter ) )

    plt.figure( f'Butterworth | N={N}' )
    plt.subplot( 1, 2, 1 )
    plt.title( 'Charakterystyka czestotliwosciowa' )
    plt.plot( f, H_Butter_dB )
    plt.plot( [0, 3e5], [-3, -3], 'r-' )
    plt.plot( [0, 3e5], [-40, -40], 'r-' )
    plt.plot( [f0/2, f0/2], [20, -160], 'r-' )
    plt.plot( [f0, f0], [20, -160], 'r-' )
    plt.grid( True )

    plt.subplot( 1, 2, 2 )
    plt.title( 'Rozklad biegunow' )
    _, p, _ = sig.butter( N, w3dB, output='zpk', analog=True )
    plt.plot( p.real, p.imag, 'ro' )
    plt.grid( True )
    plt.axis( 'equal' )
    plt.show()
 
    wiad = f'''
Butterworth zafalowania dla 64kHz: {H_Butter_dB[ int(f0//2) ]}
Butterworth tlumienie dla 128kHz: {H_Butter_dB[ int(f0) ]}'''
    print( wiad )
'''
# Sprawdzanie dla roznych ilosci biegunow
for i in range(1,20):
    butterDlaN(i)
'''
# Najoptymalniejsze
butterDlaN( 7 )

# Czebyszew 1 --------------------------------------------
def czeb1DlaN( N ):
    bn, an = sig.cheby1( N, 3, w3dB, analog=True )
    Y_jw = np.polyval( bn, 1j*w )
    X_jw = np.polyval( an, 1j*w )
    H_czeb1 = Y_jw / X_jw
    H_czeb1 = H_czeb1 / np.max( np.abs( H_czeb1 ) )
    H_czeb1_dB = 20 * np.log10( np.abs( H_czeb1 ) )

    plt.figure( f'Czebyszew 1 | N={N}' )
    plt.subplot( 1, 2, 1 )
    plt.title( 'Charakterystyka czestotliwosciowa' )
    plt.plot( f, H_czeb1_dB )
    plt.plot( [0, 3e5], [-3, -3], 'r-' )
    plt.plot( [0, 3e5], [-40, -40], 'r-' )
    plt.plot( [f0/2, f0/2], [20, -160], 'r-' )
    plt.plot( [f0, f0], [20, -160], 'r-' )
    # Dla lepszej dokladnosci
    #plt.xlim( 30e3, 130e3 )
    #plt.ylim( -50, 0 )
    plt.grid( True )

    plt.subplot( 1, 2, 2 )
    plt.title( 'Rozklad biegunow' )
    _, p, _ = sig.cheby1( N, 3, w3dB, output='zpk', analog=True )
    plt.plot( p.real, p.imag, 'ro' )
    plt.grid( True )
    plt.axis( 'equal' )
    plt.show()
 
    wiad = f'''
Czebyszew 1 zafalowania dla 64kHz: {H_czeb1_dB[ int(f0//2) ]}
Czebyszew 1 tlumienie dla 128kHz: {H_czeb1_dB[ int(f0) ]}'''
    print( wiad )

'''
# Sprawdzanie dla roznych ilosci biegunow
for i in range(1,20):
    czeb1DlaN(i)
'''
# Najoptymalniejsze
czeb1DlaN( 4 )
czeb1DlaN( 5 )

# Czebyszew 2 --------------------------------------------
def czeb2DlaN( N ):
    bn, an = sig.cheby2( N, 40, w3dB, analog=True )
    Y_jw = np.polyval( bn, 1j*w )
    X_jw = np.polyval( an, 1j*w )
    H_czeb2 = Y_jw / X_jw
    H_czeb2 = H_czeb2 / np.max( np.abs( H_czeb2 ) )
    H_czeb2_dB = 20 * np.log10( np.abs( H_czeb2 ) )

    plt.figure( f'Czebyszew 2 | N={N}' )
    plt.subplot( 1, 2, 1 )
    plt.title( 'Charakterystyka czestotliwosciowa' )
    plt.plot( f, H_czeb2_dB )
    plt.plot( [0, 3e5], [-3, -3], 'r-' )
    plt.plot( [0, 3e5], [-40, -40], 'r-' )
    plt.plot( [f0/2, f0/2], [20, -160], 'r-' )
    plt.plot( [f0, f0], [20, -160], 'r-' )
    # Dla lepszej dokladnosci
    #plt.xlim( 30e3, 130e3 )
    #plt.ylim( -50, 0 )
    plt.grid( True )

    plt.subplot( 1, 2, 2 )
    plt.title( 'Rozklad biegunow' )
    _, p, _ = sig.cheby2( N, 3, w3dB, output='zpk', analog=True )
    plt.plot( p.real, p.imag, 'ro' )
    plt.grid( True )
    plt.axis( 'equal' )
    plt.show()
 
    wiad = f'''
Czebyszew 2 zafalowania dla 64kHz: {H_czeb2_dB[ int(f0//2) ]}
Czebyszew 2 tlumienie dla 128kHz: {H_czeb2_dB[ int(f0) ]}'''
    print( wiad )

'''
# Sprawdzanie dla roznych ilosci biegunow
for i in range(1,20):
    czeb2DlaN(i)
#'''
# Najoptymalniejsze
czeb2DlaN( 5 )

# Eliptyczny ---------------------------------------------
def eliptycznyDlaN( N ):
    bn, an = sig.ellip( N, 3, 40, w3dB, analog=True )
    Y_jw = np.polyval( bn, 1j*w )
    X_jw = np.polyval( an, 1j*w )
    H_elip = Y_jw / X_jw
    H_elip = H_elip / np.max( np.abs( H_elip ) )
    H_elip_dB = 20 * np.log10( np.abs( H_elip ) )

    plt.figure( f'Eliptyczny | N={N}' )
    plt.subplot( 1, 2, 1 )
    plt.title( 'Charakterystyka czestotliwosciowa' ) 
    plt.plot( f, H_elip_dB )
    plt.plot( [0, 3e5], [-3, -3], 'r-' )
    plt.plot( [0, 3e5], [-40, -40], 'r-' )
    plt.plot( [f0/2, f0/2], [20, -160], 'r-' )
    plt.plot( [f0, f0], [20, -160], 'r-' )
    # Dla lepszej dokladnosci
    #plt.xlim( 30e3, 130e3 )
    #plt.ylim( -50, 0 )
    plt.grid( True )

    plt.subplot( 1, 2, 2 )
    plt.title( 'Rozklad biegunow' )
    _, p, _ = sig.ellip( N, 3, 40, w3dB, output='zpk', analog=True )
    plt.plot( p.real, p.imag, 'ro' )
    plt.grid( True )
    plt.show()
    
    wiad = f'''
Eliptyczny zafalowania dla 64kHz: {H_elip_dB[ int(f0//2) ]}
Eliptyczny tlumienie dla 128kHz: {H_elip_dB[ int(f0) ]}'''
    print( wiad )

'''
# Sprawdzanie dla roznych ilosci biegunow
for i in range(1,20):
    eliptycznyDlaN(i)
'''
# Najoptymalniejsze
eliptycznyDlaN( 3 )
