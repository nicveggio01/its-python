def vowelRemover(v:str) -> str:

    if not v:
        return 0
    if v[0].lower in ["a", "e", "i", "o", "u"]:
        