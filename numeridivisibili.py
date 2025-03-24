n:int=int(input("inserisci un valore n intero positivo"))
if n < 0:
    print("errore: n deve essere positivo!")
elif n % 1 != 0:
    print("errore: n deve essere intero")
else:
    counter=0
    i=0
    for i in range(10):
        x:int=int(input(f"inserisci il {i + 1}° numero intero"))
        if x % n == 0:
            counter += 1
            print(f"i numeri divisibili per n sono: {counter} ")

    


    
