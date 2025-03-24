valoreA:int=input("inserisci valore intero A > 0 and A < B")
valoreB:int=input("inserisci valore intero B > 0")

if valoreA <= 0 and valoreB <=0:
    print("errore: entrambi i valori devono essere positivi")
elif valoreA >= valoreB:
    print("errore: valore A deve essere minore di valore B")
else:
    somma=sum(range(valoreA, valoreB + 1))

print(f"la somma dei numeri tra {valoreA} e {valoreB} è: {somma}")




