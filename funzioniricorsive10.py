def charDuplicator(s:str) -> str:
    
    if s == "":
        return ""
    else:
        return s[0]*2 + charDuplicator(s[1:])
                                
print(charDuplicator("libro"))
print(charDuplicator("gatto"))
print(charDuplicator("cane"))