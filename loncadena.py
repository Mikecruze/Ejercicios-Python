def longitud(cadena):
    lon=0
    for i in cadena:
        lon+=1
    return(lon)
cadena=input("Ingresa una cadena> ")    
print (longitud(cadena))
