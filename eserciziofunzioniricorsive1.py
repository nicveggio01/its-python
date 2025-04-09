def recursivePower(base:int, esponente:int)-> int:
    if esponente == 0:
        return 1
    elif base==0:
        return 0
    else:
        return int(base*recursivePower(base, esponente-1))

print(f"3^4: {recursivePower(3,4)}")
print(f"4^3: {recursivePower(4,3)}")
print(f"2^5: {recursivePower(2,5)}")
print(f"5^2: {recursivePower(5,2)}")

