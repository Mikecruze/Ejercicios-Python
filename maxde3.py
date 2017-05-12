def max_de_3(a,b,c):
    if(a>b>c):
        return a
    if(b>c>a):
        return b
    else:
        return c
a= input("Ingrese un valor>")
b= input("Ingrese un valor>")
c= input("Ingrese un valor>")

print("El mayor es ",max(a,b,c))
