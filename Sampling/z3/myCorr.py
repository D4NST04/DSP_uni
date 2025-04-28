import numpy as np

def corr( x, y ):
    n = len( x )
    m = len( y )

    if n > m:
        y = np.pad(y, (0, n - m), mode='constant')
    elif m > n:
        x = np.pad(x, (0, m - n), mode='constant')

    result = np.zeros( n + m - 1 )

    for k in range( -n+1, m ):
        if k < 0:
            xD = np.sum( x[:k] * y[-k:] )
        else:
            xD = np.sum( x[k:] * y[:n-k] )
        
        result[ k+n-1 ] = xD

    return result
