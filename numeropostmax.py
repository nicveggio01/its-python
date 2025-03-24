numero_postimax:int=int(input("inserisci il numero postimax: "))
numero_postioccupati:int=0
opzione:str=["ingresso", "uscita", "stato", "esci"]
opzione:str=input("inserisci opzione: ")

match opzione:
    case "ingresso":
        if numero_postimax > 0:
            numero_postioccupati += 1
            print(f"posti rimanenti {numero_postimax-numero_postioccupati}")
        else:
            print("posti esauriti")
    case "uscita":
        if numero_postioccupati > 0:
            numero_postioccupati -= 1
            print(f"posti rimanenti {numero_postimax-numero_postioccupati}")
    case "stato":
        if numero_postioccupati > 0:
         print(f"posti rimanenti {numero_postimax - numero_postioccupati}")
         print(f"posti occupati {numero_postioccupati}")
    case "esci":
        print("ciao")
    case _:
        print("comando non valido")