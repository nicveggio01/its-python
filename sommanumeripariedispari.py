# inserire un numero variabile di numeri interi scelto dall'utente

n:int=int(input("quanti numeri desideri inserire?"))

numeri=[]
 
for i in range(n):
    n= int(input("inserisci il numero {i+1}: "))
    numeri.append(n)

media= sum(numeri)/len(numeri)

media=0
somma_pari=0
somma_dispari=0

if n % 2 == 0 and n > media:
    somma_pari += n
elif n % 2 !=0 and n < media:
    somma_dispari= sum(numeri % 2 != 0)
    somma_dispari += n

print(f" la somma dei numeri pari e maggiori della media è: {somma_pari} ")
print(f" la somma dei numeri dispari e minori della media è: {somma_dispari} ")


if somma_pari > somma_dispari:
    print("la somma pari è maggiore di quella dispari")
elif somma_pari < somma_dispari:
    print("la somma pari è minore di quella dispari")
else:
    print("la somma pari è uguale a quella dispari")
