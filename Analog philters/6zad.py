import numpy as np 
from matplotlib import pyplot as plt 
from scipy import signal as sig 

# Parametry
f_s = 256e3
f0 = f_s/2 
f3dB = f0/2 
w0 = 2*np.pi*f0
w3dB = 2*np.pi*f3dB
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
    #print( wiad )
'''
# Sprawdzanie dla roznych ilosci biegunow
for i in range(1,20):
    butterDlaN(i)
'''
# Najoptymalniejsze
butterDlaN( 7 )

# Sprzetowa implementacja ==========================================
# Parametry filtru
N = 7               # Rzad filtru
fc = 256_000        # Czestotliwosc graniczna [Hz]
w0 = 2*np.pi*fc     # -||- [rad/s]

# Liczymy bieguny
z, p, k = sig.butter( N, 1, analog=True, output='zpk' )
# ZPK -> na ciagi bm i an 
b, a = sig.zpk2tf( z, p, k )
# podzial na sekcje 2 rzedu
sos = sig.tf2sos( b, a )

C = 10e-9 # 10 nF
R_wartosci = []
skala = 2*np.pi*f3dB

for sekcja in sos:
    b0, b1, b2, a0, a1, a2 = sekcja
    if ( np.isclose( a2, 0 ) or np.isclose( a1, 0 ) ):
        continue
    wn_sq = a2 
    wn = np.sqrt( wn_sq )
    Q = wn / a1 

    # Skalowanie do rzeczywistej czestotliwosci
    wn_real = wn * skala 
    # Oblicz R-ki dla Sallen-Key 
    R1 = 1 / ( wn_real * C )
    R2 = Q * R1

    R_wartosci.append( [R1, R2] )

# Sekcja 1 rzedowa ( ostatnia )
R1_1 = 1 / ( 2*np.pi*fc*C )

H_spr = 1 
s = 1j*w
# Wyświetl
print("Sekcje Sallen-Key (2 rzędu):")
for i, (R1, R2) in enumerate(R_wartosci):
    print(f"Sekcja {i+1}: R1 = {R1:.1f} Ω, R2 = {R2:.1f} Ω, C1 = C2 = 10 nF")
    licznik = 1/( R1*R2*C*C )
    mianownik = s*s + (1/( R1*C )  + 1/( R2*C ) )*s + 1/( R1*R2*C*C )
    H_cz = licznik / mianownik
    H_spr = H_spr * H_cz 


print("\nSekcja 1-rzędowa (RC):")
print(f"R = {R1_1:.1f} Ω, C = 10 nF")
licznik = 1/( R1_1*C )
mianownik = s + 1/( R1_1*C )
H_cz = licznik / mianownik
H_spr = H_spr * H_cz
H_spr = H_spr / np.max( np.abs( H_spr ) )

H_spr_dB = 20*np.log10( np.abs( H_spr ) )

plt.figure( f'Butterworth projekt | N={N}' )
plt.title( 'Charakterystyka czestotliwosciowa' )
plt.plot( f, H_spr_dB )
plt.plot( [0, 3e5], [-3, -3], 'r-' )
plt.plot( [0, 3e5], [-40, -40], 'r-' )
plt.plot( [f0/2, f0/2], [20, -160], 'r-' )
plt.plot( [f0, f0], [20, -160], 'r-' )
plt.grid( True )
plt.show()
'''
# Opcjonalnie: rysuj charakterystykę
w, h = sig.butter(N, w0, analog=True, output='ba')
w_plot, h_plot = np.logspace(3, 6, 1000), []
for w_i in w_plot:
    s = 1j * 2 * np.pi * w_i
    Y_jw = np.polyval( np.atleast_1d( h[0] ), s )
    X_jw = np.polyval( np.atleast_1d( h[1] ), s )
    H = Y_jw / X_jw
    h_plot.append(H)

plt.semilogx(w_plot, 20 * np.log10(np.abs(h_plot)))
plt.title('Charakterystyka filtru Butterwortha N=7')
plt.xlabel('Częstotliwość [Hz]')
plt.ylabel('Amplituda [dB]')
plt.grid(which='both', axis='both')
plt.show()
'''
