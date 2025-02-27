animali= input("Inserisci il nome di un animale: ")

match animali:

    case ["cane", "gatto", "cavallo", "elefante", "leone"]:
        print("L'animale inserito è un mammifero")
    case ["serpente", "lucertola", "tartaruga", "coccodrillo"]:
        print("L'animale inserito è un rettile")
    case ["aquila", "pappagallo", "gufo", "falco"]:
        print("L'animale inserito è un uccello")
    case ["squalo", "trota", "salmone", "carpa"]:
        print("L'animale inserito è un pesce")
    case _:
        print("L'animale inserito non è presente nella lista") 