def name_to_bits():
    name = input( 'Podaj imie: ')
    with open( './bits.txt', 'w+' ) as zapis:
        for letter in name:
            '''
            print( "Litera: " + letter )
            print( "Numer litery: " + str( ord( letter ) ) )
            print( bin( ord( letter ) )[2:] )
            print( "Binarnie: " + str( bin( ord( letter ) ) ) , end='\n\n')
            '''
            inBin = bin( ord( letter ) )[2:]
            while len( inBin ) < 8:
                inBin = "0" + inBin 

            zapis.write( inBin )
            print( inBin )
