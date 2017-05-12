def max(x,y):
    if(x>y):
        return x
    elif(y>x):
        return y
    else:
        print("Son iguales")

x=input("Ingrese un valor>")

y=input("Ingrese otro valor>")
print ("El número mayor es: ",max(x,y))
