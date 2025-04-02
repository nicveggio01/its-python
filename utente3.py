class utente:
    def __init__(self, first_name: str, last_name: str, nome_utente:str, email:str):
        self.first_name= first_name
        self.last_name= last_name
        self.nome_utente= nome_utente
        self.email= email

    def describe_user(self):
        print(f"nome:{self.first_name}, cognome: {self.last_name} nome_utente: {self.nome_utente}, email: {self.email}  ")
    def greet_user(self):
        print(f" ciao {self.first_name} {self.last_name} benvenuto!")



class privilegi:
    def __init__(self, lettura: str, scrittura: str, esecuzione: str):
        self.lettura= lettura
        self.scrittura=scrittura
        self.esecuzione=esecuzione
    
    def show_privilegi(self): 
        print(f"privilegio1: {self.lettura}, privilegio2:{self.scrittura}, privilegio3:{self.esecuzione}")

class admin:
    def __init__(self, utente: utente, privilegi: privilegi):
        self.utente=utente
        self.privilegi= privilegi


    def display_info_utente(self):
        self.utente.describe_user()


    def display_privilegi(self):
        self.privilegi.show_privilegi()

