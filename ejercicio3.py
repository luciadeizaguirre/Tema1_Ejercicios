lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3=[]
for i in lista_1:
    if(i not in lista_3) and i in lista_2:
        lista_3.append(i)
print(lista_3)

#Con programacion funcional
def repeticiones(lista_1,lista_2):
    for i in lista_1:
        for j in lista_2:
            if i==j:
                lista_3.append(i)
    lista_3=list(tuple(lista_3))
    return lista_3

