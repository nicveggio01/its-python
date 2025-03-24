n = int(input("Inserisci un numero n: "))

# Verifica se n è negativo
if n < 0:
    print("n è negativo! Inserisci un numero positivo.")
else:
    
    if n % 2 == 0:
        somma = 0
        for i in range(1, n + 1): 
            if i % 4 == 0:
                somma += i 
        print(f"La somma dei numeri da 1 a {n} divisibili per 4 è: {somma}")

    
    else:
        if n == 1:
            
            prodotto = 1
        else:
            prodotto = 1
            for i in range(1, n + 1, 2):  
                prodotto *= i 
        print(f"Il prodotto dei numeri dispari da 1 a {n} è: {prodotto}")

