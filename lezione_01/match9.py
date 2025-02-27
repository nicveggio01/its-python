lancio_moneta=1
lancio_croce=0
lancio_testa=0

while lancio_moneta <= 8: 
    print(f"Lancio numero {lancio_moneta}")
    risutato_lancio = input("inserire il risultato del lancio con T o C (t |c utilizzabili:)")
    lancio_moneta += 1
    match risutato_lancio:
        case "T | t":
            lancio_testa += 1
        case "C | c":
            lancio_croce += 1
        case _:
            print("Error")

print(f"in otto lanci sono uscite {lancio_testa} teste e {lancio_croce} croci, con una percentuale di {lancio_testa/8*100}% teste e {lancio_croce/8*100}% croci")