print("¡Hola! Cristal, Eduardo, Jasmín y Mauricio te dan la bienvenida al bar más chido de la ciudad.")
nombre =(input("Cómo te llamas?"))
edad =int(input(nombre + ", ¿Cuál es tu edad?"))
if edad < 18: print("No puedes entrar")
elif edad > 65: print("te recibimos en el espacio especial")
elif edad == 40: print("Te ganaste una chela.")
elif edad >= 41 and edad <= 50:
        print("participa en el salón de los 90")
else: print("puedes entrar")

saldo =int(input("¿Cuánta feria traes?"))
if saldo >0 and saldo <1000: 
 print("¡Eres pobre y no puedes jugar!")
elif saldo >1000 and saldo <3000:
    print("puedes jugar lotería")

bailar =input("¿Te gusta bailar?")
if bailar == "no":
    print ("¿A qué bienes, amiguis?")
elif bailar == "si":
    print ("¡diviértete mil!")