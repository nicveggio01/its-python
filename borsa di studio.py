reddito:float=float(input("inserisci reddito familiare:"))
media:float=float(input("inserisci media dei voti:"))
if reddito < 20000 and media > 27:
    print("hai diritto alla borsa di studio")
else:
    print("non hai diritto alla borsa di studio")
    