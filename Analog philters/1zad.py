import numpy as np 
from matplotlib import pyplot as plt
from scipy import signal as sig 

# Zera i bieguny
z = [ 5j, 
     -5j, 
     15j, 
     -15j ]

p = [-0.5 + 9.5j,
     -0.5 - 9.5j,
     -1 + 10j,
     -1 - 10j,
     -0.5 + 10.5j,
     -0.5 - 10.5j ]

w = np.linspace( 0.1, 20, 199, endpoint=False )

# Licznik transmitancji ( osłabiający )
bn = np.poly( z )
Y_jw = np.polyval( bn, 1j*w )
# Mianownik transmitancji ( wzmacniajacy )
an = np.poly( p )
X_jw = np.polyval( an, 1j*w )

# Wynikowa transmitancja
H = Y_jw / X_jw                     # Liniowa
H_dB = 20 * np.log10( np.abs( H ) ) # Logarytmiczna

plt.plot( np.real( z ), np.imag( z ), 'ro' )
plt.plot( np.real( p ), np.imag( p ), 'b*' )
plt.title( 'Zera i bieguny na plaszczyznie' )
plt.xlabel( 'Real' )
plt.ylabel( 'Imaginary' )
plt.grid()
plt.show()

plt.subplot( 1, 2, 1 )
plt.plot( w, np.abs( H ), 'b' )
plt.title( 'Cha-ka amp-cz liniowa' )
plt.xlabel( 'w [rad/s]' )
plt.ylabel( '|H(jw)|' )
plt.grid()

plt.subplot( 1, 2, 2 )
plt.plot( w, H_dB, 'b' )
plt.title( 'Cha-ka amp-cz logarytmiczna' )
plt.xlabel( 'w [rad/s]' )
plt.ylabel( '20log10(|H(jw)|)' )
plt.grid()

plt.show()

# Punkt odniesienia do normalizacji (np. omega = 10 rad/s)
omega_ref = 10  # Mo?na zmieni? na dowolne omega, np. w centrum pasma

# Oblicz warto?? H(jw) w tym punkcie
jw_ref = 1j * omega_ref
H_ref = np.polyval(bn, jw_ref) / np.polyval(an, jw_ref)

# Skaluj?cy wsp?czynnik
K = 1 / np.abs(H_ref)

# Przemn? licznik przez K
bn_scaled = K * bn

# Licz now? odpowied? cz?stotliwo?ciow?
Y_jw_scaled = np.polyval(bn_scaled, 1j*w)
H_scaled = Y_jw_scaled / X_jw
H_scaled_dB = 20 * np.log10( np.abs( H_scaled ) )

# Wykresy po skalowaniu
plt.subplot( 1, 2, 1 )
plt.plot( w, np.abs( H_scaled ), 'b' )
plt.title( 'Cha-ka amp-cz liniowa (skalowana)' )
plt.xlabel( 'w [rad/s]' )
plt.ylabel( '|H(jw)|' )
plt.grid()

plt.subplot( 1, 2, 2 )
plt.plot( w, H_scaled_dB, 'b' )
plt.title( 'Cha-ka amp-cz logarytmiczna (skalowana)' )
plt.xlabel( 'w [rad/s]' )
plt.ylabel( '20log10(|H(jw)|)' )
plt.grid()

plt.show()


'''
# Normalizacja transmitancji
H2 = H / np.max( np.abs( H ) )
H2_dB = 20 * np.log10( np.abs( H2 ) )

plt.subplot( 1, 2, 1 )
plt.plot( w, np.abs( H2 ), 'b' )
plt.title( 'Cha-ka amp-cz liniowa v2' )
plt.xlabel( 'w [rad/s]' )
plt.ylabel( '|H(jw)|' )
plt.grid()

plt.subplot( 1, 2, 2 )
plt.plot( w, H2_dB, 'b' )
plt.title( 'Cha-ka amp-cz logarytmiczna v2' )
plt.xlabel( 'w [rad/s]' )
plt.ylabel( '20log10(|H(jw)|)' )
plt.grid()

plt.show()
'''
# Ale bedzie faza zaraz
faza = np.atan( np.imag(H) / np.real(H) )

plt.stem( w, faza, 'k-' )
plt.title( "Cha-ka faz-czest" )
plt.xlabel( 'Czestotliwosc znormalizowana' )
plt.ylabel( 'Faza [rad]' )
plt.show()

w, h = sig.freqz( bn, an )
faza = np.angle( h )

plt.plot( w, faza )
plt.title( 'Odpowiedz fazowa' )
plt.grid()
plt.show()


plt.show()
