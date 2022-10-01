list=[input("Escriba los caracteres separados por comas que quiere en la lista: ").split()]
lista=str(list)
def agregar_una_vez(lista):
    elemento:input("Escriba un elemento nuevo para agregar a la lista: ")
    if elemento in lista:
        print("Error: Imposible añadir elementos duplicados =>" [elemento])   
    else:
        lista.append(elemento)
    return lista

    print(lista)

