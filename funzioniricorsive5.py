def recursiveArmonicProgression(n:int) -> float:
    if n == 1:
        return 1
    elif n <= 0:
       return 0 
    else:
        return 1.0/ n + recursiveArmonicProgression(n-1)
    
print(recursiveArmonicProgression(6))