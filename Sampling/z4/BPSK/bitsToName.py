def BTN( tab ):
    imie = ""
    for i in range( 0, len( tab ), 8 ):
        znak = ''.join(str(x) for x in tab[i:(i+8)])
        imie += chr(int(znak,2))
    return imie
