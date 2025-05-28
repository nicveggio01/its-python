from Book import Book

if __name__=='__main__':
    book_str= "La Divina Commedia, D. Alighieri, 999990066"
    divina_commedia: Book= Book.from_string(book_str)
    print(divina_commedia)