n:int=int(input("Enter a number: "))

if n >= 0:

    fattoriale=1
    for i in range(1,n+1):
        fattoriale=fattoriale*i
    print("Il fattoriale di",n,"è",fattoriale)
else:
    print("Il fattoriale di",n,"non è definito")
    