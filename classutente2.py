class utente:
    def __init__(self, first_name: str, last_name: str, login_attempts:int):
        self.first_name= first_name
        self.last_name= last_name
        self.login_attempts= login_attempts

    def describe_user(self):
        print(f"nome:{self.first_name}, cognome: {self.last_name} ")
    def greet_user(self):
        print(f" ciao {self.first_name} {self.last_name} benvenuto!")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts=0


user=utente("niccolo", "veggian", 0)
print(user.first_name)
print(user.last_name)

user.describe_user()
user.greet_user()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(f"numero di tentativi: {user.first_name}: {user.login_attempts}")

user.reset_login_attempts()

print(f"numero di tentativi {user.first_name} dopo il reset: {user.login_attempts} ")