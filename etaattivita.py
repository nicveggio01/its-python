eta:int=int(input("inserisci la tua età"))
if 18 < eta < 65:
    print("l'utente può partecipare all'attività")
elif eta < 18:
    print("non puoi partecipare all'attività: età minima consentita 18 anni")
else:
    print("non puoi partecipare all'attività: età massima consentita 65 anni")
    