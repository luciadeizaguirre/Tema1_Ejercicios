numero_a_descomponer=int(input("Escriba un numero entero: "))
cadena=str(numero_a_descomponer)
print(cadena[3].zfill(4))
print(cadena[2].zfill(3)+"O")
print(cadena[1].zfill(2)+"00")
print(cadena[0]+"000")
