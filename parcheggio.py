sedielibere:int=20
sedieoccupate:int=0
opzione:str=["prenota", "libera", "visualizza", "esci"]
opzione:str=input("Inserisci opzione: ")

match opzione:
    case "prenota":
        if sedieoccupate < sedielibere:
            sedieoccupate+=1
            print("Prenotazione effettuata")
        else:
            print("Non ci sono posti disponibili")
    case "libera":
        if sedieoccupate > 0:
            sedieoccupate-=1
            print("Prenotazione liberata")
        else:
            print("Non ci sono posti occupati")
    case "visualizza":
        print(f"sedie libere: {sedielibere-sedieoccupate}")
        print(f"sedie occupate: {sedieoccupate}")
    case "esci":
        print("Arrivederci")
    case _:
        print("Comando non valido")
        
        
