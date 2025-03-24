somma=0
n = int(input("Inserisci un numero intero: "))
 
if 1 <= n <= 100:
    somma_pari = sum(i for i in range(2, n+1, 2))
    print(f"la somma dei numeri pari compresi fra 1 ed {n} è:{somma_pari}")
elif n <= 0:
    print("errore: n deve esere positivo")
else:
    somma_dispari= sum(i for i in range(1, n+1, 2))
    print(f"la somma dei numeri dispari compresi fra 1 ed {n} è: {somma_dispari}")
    

