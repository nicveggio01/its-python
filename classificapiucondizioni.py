
n:int=int(input("inserisci un valore intero"))
if n % 1 != 0:
    print("errore inserire un valore intero!")
elif n % 2 == 0 and n >= 10:
    print("numero non valido!")
else:
    print("numero valido")
    