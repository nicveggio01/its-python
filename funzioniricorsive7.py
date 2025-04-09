def recursiveProduttoria(n:int) -> int:
    if n <= 0:
        return 1
    else:
        return (n**3)*recursiveProduttoria(n-1)
    
print(recursiveProduttoria(5))