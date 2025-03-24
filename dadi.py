punteggio:int=0
somma:int=0

while punteggio < 100:

  d1:int=int(input("inserisci un valore compreso o uguale tra 1 e 6 "))
  d2:int=int(input("inserisci una valore compreso o uguale tra 1 e 6"))

  if 1 <= d1 <= 6 and 1 <= d2 <= 6:
    somma= d1+d2
    if d1 ==0 and d2 % 2 == 0 and somma > 8:
      punteggio= 100
      print("punteggio:100 hai vinto!")
    elif d1 or d2== 6 or somma==7:
      punteggio += 10
    else: 
      punteggio=0
      print("hai perso!")
