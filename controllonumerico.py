x:int=int(input("inserisci un numero x intero positivo"))
y:int=int(input("inserisci un numero y intero positivo"))
z:int=int(input("inserisci un numero z intero positivo"))

if x < 0 and x % 1 != 0:
    print("x deve essere intero positivo!")
elif y < 0 and y % 1 != 0:
    print("y deve essere intero positivo!")
elif z < 0 and z % 1 !=0:
    print("z deve essere intero positivo!")

else:
 if int(sum ([x+y+z])) % 2 == 0:
    if x % 3 != 0:
        print("x deve essere divisibile per 3")
    elif y % 5 != 0:
        print("y deve essere divisibile per 5")
    elif z % 7 != 0:
        print ("z deve essere divisibile per 7")
    else:
        print("regole rispettate!")
 else:
     print("la somma di x, y, z deve essere pari")
  
