lista=[1,2,13,23,3,26,6]
lista_pares=[]
lista_impares=[]
def separar(lista):
    for i in lista:        
        if i % 2 == 0:
            lista_pares.append(i)
        else:
            lista_impares.append(i)
            return(lista)  
    print(lista_pares)
    print(lista_impares)
