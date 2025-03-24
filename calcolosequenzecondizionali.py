n:int=int(input("inserisci un numero n"))

if n < 0:
    print("n è negativo! inserisci un numero positivo")
else:
    if n % 2 == 0: # consideriamo numeri pari
        somma=0
        for i in range(1, + n + 1):
            if i % 4 == 0:
                somma += i
    print(f" la somma dei numeri da 1 ad {n} e divisibili per 4 è: {somma} ")
    
    if n % 2 != 0:
        prodotto = 1
        for i in range(1, n + 1, 2):  # Consideriamo solo numeri dispari
            prodotto *= i
        print(f"Il prodotto dei numeri dispari da 1 a {n} è: {prodotto}")

      
