import random

numero_secreto = random.randint(1, 10)
intento = 0

while intento != numero_secreto:
    intento = int(input("Adivina el número entre 1 y 10: "))

    if intento < numero_secreto:
        print("Muy bajo, intenta de nuevo")
    elif intento > numero_secreto:
        print("Intento muy alto, intenta de nuevo")

print("¡Adivinaste! El número era", numero_secreto)