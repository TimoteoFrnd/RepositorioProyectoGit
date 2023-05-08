def piramide():  #Definimos la funcion piramide

    numero = int(input('Digite um número: '))  #

    for p in range(0, numero):

        print("*" * p)
    
    print("*" * numero)

    for p in reversed(range(0, numero)):

        print("-" * p)

piramide()