max_posti_liberi=100
posti_occupati=0
while True:
    nome_corso = input("inserisci il nome del corso")
    opzione = input("inserisci l'opzione desiderata(iscrivi,visualizza,annulla,elimina,esci)")

    if opzione == "iscrivi":
        if max_posti_liberi > 0:
            print(f"Iscrizione al corso {nome_corso} completata.")
            max_posti_liberi-=1
            posti_occupati+=1
        else:
            print("Non ci sono posti disponibili.")
    if opzione == "annulla":
        if max_posti_liberi < 100:
            max_posti_liberi += 1
            posti_occupati-=1
            print("operazione annullata")
        else:
            print("tutti i posti sono già disponibili") 
    if opzione == "visualizza":
       print(f"posti liberi:{max_posti_liberi-posti_occupati}") 
       print(f"posti occupati: {posti_occupati}")
    if opzione == "elimina":
        print(f"{nome_corso} eliminato")
    if opzione == "esci":
        print("arrivederci")
        break
    else:
        print("opzione non valida")
