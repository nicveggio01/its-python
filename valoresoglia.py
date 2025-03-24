soglia:int=int(input("inserisci valore soglia: "))
n:int=int(input("inserisci 7 numeri: "))
count=0
while n!=0:
    if n>soglia:
        count+=1
        print("il numero",n,"è maggiore della soglia")
    else:
        count=count
        print("il numero",n,"è minore della soglia")
    n=int(input())
print("il numero di numeri maggiori della soglia è",count)
print("il numero di numeri minori della soglia è",7-count)




