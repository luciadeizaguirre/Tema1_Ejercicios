numero_magico=12345679
numero_usuario=int(input("Introduce un numero: "))
if numero_usuario >9 or numero_usuario < 0:
    print("Numero no valido")
else:
    multiplicación1=numero_usuario * 9
    multiplicacion2 = numero_magico * multiplicación1
print(multiplicacion2)
