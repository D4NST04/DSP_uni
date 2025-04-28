import numpy as np 
from matplotlib import pyplot as plt 
from scipy import signal as sig 

def sprawdz( N, filtr, zmiana ):
    # Listing 7.4 ===============================================
    # Wymagania
    #N = 8       # Liczba biegunow transmitancji
    f0 = 100    # Dla filtrow LP i HP 
    f1 = 10     # Dla filtrow BP i BS
    f2 = 200    # Dla filtrow BP i BS
    Rp = 3      # Dozwolony poziom oscylacji w pasmie przepustowym - ripples in pass
    Rs = 100    # Dozwolony poziom oscylacji w pasmie zaporowym - ripples in stop

    # Projekt filtra analogowego - LP z w0=1
    if filtr == 1:
        z, p, wzm = sig.cheb1ap( N, Rp )        # an. prot. Czebyszewa 1
    elif filtr == 2:
        z, p, wzm = sig.cheb2ap( N, Rs )        # an. prot. Czebyszewa 2
    elif filtr == 3:
        z, p, wzm = sig.ellipap( N, Rp, Rs )    # an. prot. Eliptyczny
    else:
        z, p, wzm = sig.buttap( N )             # an. prot. Butterworth

    b = np.atleast_1d( wzm * np.poly( z ) )
    a = np.poly( p )
    f = np.linspace( 0, 1000, int(1e5), endpoint=False )
    w = 2 * f * np.pi 

    Y_jw = np.polyval( b, 1j*w )
    X_jw = np.polyval( a, 1j*w )
    H = Y_jw / X_jw
    H_dB = 20 * np.log10( np.abs( H ) )


    r = np.max( np.abs( np.concatenate([z, p]) ) )
    fi = np.linspace(0, 2*np.pi, 2000, endpoint=False)
    c = r * np.cos(fi)
    s = r * np.sin(fi)
    
    plt.figure( 'Analog proto |H(f)|' )
    plt.semilogx( w, H_dB )
    plt.grid( True )
    plt.xlabel( 'w [rad*Hz]' )
    plt.show()

    plt.figure( 'Analog proto ZP' )
    plt.plot( np.real( z ), np.imag( z ), 'ro' )
    plt.plot( np.real( p ), np.imag( p ), 'b*' )
    plt.plot( c, s, 'k-' )
    plt.grid( True )
    plt.show()

    if zmiana == 1:
        b, a = sig.lp2hp( b, a, 2*f0*np.pi )
    elif zmiana == 2:
        b, a = sig.lp2bp( b, a, 2*np.pi*np.sqrt( f1*f2 ), 2*np.pi*np.sqrt( f2-f1 ) )
    elif zmiana == 3:
        b, a = sig.lp2bs( b, a, 2*np.pi*np.sqrt( f1*f2 ), 2*np.pi*np.sqrt( f2-f1 ) )
    else:
        b, a = sig.lp2lp( b, a, 2*f0*np.pi )
    z = np.roots( b )
    p = np. roots( a )

    # Listing 7.1 ===============================================
    '''
    # Zaprojektuj/dobierz wspolczynniki transmitancji filtra analogowego
    flaga = False 
    if flaga:
        b = np.array( [ 3, 2 ] )
        a = np.array( [ 4, 3, 2, 1 ] )
        z = np.roots( b )
        p = np.roots( a )
    else:
        wzm = 0.001
        z = 2j*np.pi* np.array( [ 100, 200 ] )
        z = np.concatenate( [ z, np.conj( z ) ] )
        p = -2j*np.pi* np.array( [ 100, 200 ] )
        p = np.concatenate( [ p, np.conj( p ) ] )
        b = np.atleast_1d( wzm*np.poly(z) )
        a = np.poly( p )
    '''
    plt.figure( 'Zera (o) i Bieguny (*)' )
    plt.xlabel( 'Real' )
    plt.ylabel( 'Imag' )
    plt.grid( True )
    plt.plot( np.real( z ), np.imag( z ), 'bo' )
    plt.plot( np.real( p ), np.imag( p ), 'r*' )
    plt.show()

    f = np.linspace( 0, 1000, 10_000, endpoint=False )
    w = 2*f*np.pi 
    Y_jw = np.polyval( b, 1j*w )
    X_jw = np.polyval( a, 1j*w )
    H = Y_jw / X_jw
    H_dB = 20*np.log10( np.abs( H ) )

    plt.figure( '|H(f)| [dB]' )
    plt.grid( True )
    plt.xlabel( 'f [Hz]' )
    plt.plot( f, H_dB )
    plt.show()

    plt.figure( 'angle( H(f) ) [rad]' )
    plt.grid( True )
    plt.xlabel( 'f [Hz]' )
    ang = np.unwrap( np.angle(H) )
    plt.plot( f, ang )
    plt.show()


    sys = sig.TransferFunction( b, a )
    t1, y1 = sig.impulse( sys )
    t2, y2 = sig.step( sys )

    plt.figure( 'Odp impuls' )
    plt.plot( t1, y1 )
    plt.grid( True )

    plt.figure( 'Odp skok' )
    plt.plot( t2, y2 )
    plt.grid( True )

    plt.show()

'''
1 parametr: N

2 parametr:
    0 - Butterworth
    1 - Czebyszew 1 
    2 - Czebyszew 2
    3 - Eliptyczny

3 parametr 
    0 - LowPass to LowPass
    1 - LowPass to HighPass
    2 - LowPass to BandPass
    3 - LowPass to BansStop
'''

sprawdz( 4, 3, 1 ) 
