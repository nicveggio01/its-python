import random

percorso:list[str]= [for i in range (71)]

i= random.randint(1, 10)

print(i)

def mossatartaruga():
  
  t= 1

  if 1 <= i <= 5:

    mossatartaruga(i)= t + 3
    print(f"scivolata", "posizione: {mossatartaruga}")

  if 6 <= i <= 7:
    mossatartaruga(i)= t - 6
  