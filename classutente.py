class utente:
    def __init__(self, first_name: str, last_name: str):
        self.first_name= first_name
        self.last_name= last_name

    def describe_user(self):
        print(f"nome:{self.first_name}, cognome: {self.last_name} ")
    def greet_user(self):
        print(f" ciao {self.first_name} {self.last_name} benvenuto!")

utente1= utente("Niccolo", "Veggian")
print(utente1.first_name)
print(utente1.last_name)

utente1.describe_user()
utente1.greet_user()

utente2= utente("Domenico", "Candido")
print(utente2.first_name)
print(utente2.last_name)

utente2.describe_user()
utente2.greet_user()

utente3= utente("Sergio", "De guidi")
print(utente3.first_name)
print(utente3.last_name)

utente3.describe_user()
utente3.greet_user()

utente4= utente("Daniele", "Tafi")
print(utente4.first_name)
print(utente4.last_name)

utente4.describe_user()
utente4.greet_user()

utente5= utente("Paola", "Geppi")
print(utente5.first_name)
print(utente5.last_name)

utente5.describe_user()
utente5.greet_user()