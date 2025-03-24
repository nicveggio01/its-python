temperature=[]
for i in range (7):
    temp=float(input(f"inserisci la temperaturatura del giorno {i + 1} (1= lunedì, 7= domenica) "))
    temperature.append(temp)

    # calcolare la media delle temperature

    media= sum(temperature)/len(temperature)
    print(f"la media delle temperature è: {media}")

     # verificare che la temperatura sia nella norma

    if all(10 < temp < 30 for temp in temperature):
        print("temperatura nella norma")

    # verificare temperature estreme

    if any( temp > 35 or temp < 5 for temp in temperature):
        print("allerta temperatura")

    # trovare il giorno con le temperature max e min

    giorno_max= temperature.index(max(temperature)) + 1
    giorno_min=temperature.index(min(temperature)) + 1

    print(f"la temperatura più alta è stata: {giorno_max} con {max(temperature)}")
    print(f" la temperatura più bassa è stata: {giorno_min} con {min(temperature)}")