
palabra = input("Ingresa una palabra")
letra_objetivo = input("Ingresa una letra a buscar")
contador = 0

for letra in palabra:
    if letra == letra_objetivo:
        contador += 1

print(contador)
