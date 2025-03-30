class restaurant:
    def __init__(self, name:str, type:str, number_served:int, increment_number_served: int):
        self.name= name
        self.type= type
        self.number_served= number_served
        self.increment_number_served= increment_number_served

    # metodo
    def describe_restaurant(self):
        print(f" il ristorante {self.name} fa una cucina di tipo {self.type}")
    def open_restaurant(self):
        print(f" il ristorante {self.name} che fa cucina di tipo {self.type} è aperto!")
    def set_number_served(self, number):
        self.number_served= number
        print(f" il ristorante {self.name} ha servito {self.number_served} clienti")
    def increment_number_seved(self, increment):
        self.number_served += increment
        print(f" il ristorante {self.name} ha sevito {self.number_served} clienti")

restaurant1= restaurant("osaka fusion", "giapponese", 16, 20)
print(restaurant1.name)
print(restaurant1.type)
print(restaurant1.number_served)
print(restaurant1.increment_number_served)

restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant1.set_number_served(16)
restaurant1.increment_number_seved(20)
