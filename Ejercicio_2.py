#Construya un programa tal, que lea un número entero N, muestre la cantidad de términos y el resultado
#de la siguiente serie: 1-1/2+1/3-1/4+...+-1/N 

N=int(input("Ingrese un valor entero: ")) #Para solicitar un valor se escribe input pero se debe declara e tipo de variable 

if N > 0:
    suma = 0.0

    # Iteramos sobre los términos de la serie
    for i in range(1, N + 1):
        termino = 1 / i
        # Suma si el índice es impar, resta si es par
        if i % 2 == 0:
            suma -= termino
        else:
            suma += termino

    print(f"Cantidad de términos: {N}")
    print(f"Resultado de la serie: {suma:.6f}")
else:
    print("Por favor ingrese un número entero positivo.")

