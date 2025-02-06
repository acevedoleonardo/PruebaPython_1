##4 tipos de funciones

##Funcion sin parametros y sin retorno
def funcion1():
    print("Soy una funcion increible!!!!!!!")
funcion1()

##Funcion sin parametros pero con retorno
def funcion2():
    return 5
print("Su número es:",funcion2())

##Funcion con parámetros pero sin retorno
def funcion3 (nombre,apellido):
    print("Su nombre es:",nombre," ",apellido)
funcion3("Edgar","Acevedo")

##Función con parámetros y retorno
def funcion4(a,b):
    c= a**b
    return c

funcionA= int(input("Ingrese el numero base:"))
funcionB=int(input("Ingrese la elevación deseada:"))
print("El resultado de su elevación es de:",funcion4(funcionA,funcionB))

##Desarrollado por : Pedro Gomez / C.C:1.666.555.444