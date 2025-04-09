def recursiveDigitcounter(n:int,c:int=1) -> int:
    n=abs(n)
    if n < 10:
        return c 
    else:
        return recursiveDigitcounter(n//10, c+1)
    
print(recursiveDigitcounter(560))
print(recursiveDigitcounter(7899765))