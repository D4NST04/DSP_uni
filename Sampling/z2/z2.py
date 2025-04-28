import matplotlib.pyplot as plt 
import numpy as np

def sinc( x ):
    if x != 0: return (np.sin(x)/x)
    else: return 1 

# Parametry
t = 0.1
amp = 230 
f = 50
f_anal = int( 1e4 )
f_prob = 200 

wek_t_anal = np.linspace( 0, t, int(t*f_anal), False )
wek_t_prob = np.linspace( 0, t, int(t*f_prob), False )

sygnal_anal = amp * np.sin( 2*np.pi*f*wek_t_anal )
sygnal_prob = amp * np.sin( 2*np.pi*f*wek_t_prob )

wek_t_odt = np.linspace( 0, t, int(t*f_anal), False )
sygnal_odt = np.zeros( len( sygnal_anal ) )
for i in range( len(wek_t_odt) ):
    teraz = wek_t_odt[i]
    wartosc = 0
    for j in range( len(wek_t_prob) ):
        arg = np.pi*f_prob*(teraz-wek_t_prob[j])
        wartosc += ( sygnal_prob[j] * sinc(arg) )
    sygnal_odt[i] = wartosc

bledy = sygnal_anal - sygnal_odt

plt.plot( wek_t_prob, sygnal_prob, "b-o",
         label='Sygnal probkowany' )
plt.plot( wek_t_anal, sygnal_anal, "k-",
         label='Sygnal pseudo-analogowy' )
plt.plot( wek_t_odt, sygnal_odt, "g-", 
         label='Sygnal odtworzony' )
plt.plot( wek_t_odt, bledy, "r-.",
         label='Bledy odtworzenia' )

plt.legend()
plt.grid()
plt.show()
