class restaurant:
    def __init__(self, name:str, type:str):
        self.name= name
        self.type= type

    # metodo
    def describe_restaurant(self):
        print(f" il ristorante {self.name} fa una cucina di tipo {self.type}")
    def open_restaurant(self):
        print(f"il ristorante {self.name} che fa una cucina di tipo {self.type} è aperto")

restaurant1= restaurant("osaka fusion", "giapponese")
print(restaurant1.name)
print(restaurant1.type)

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2= restaurant("davì", "indiano")
print(restaurant2.name)
print(restaurant2.type)

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3= restaurant("atipiko", "greco")
print(restaurant3.name)
print(restaurant3.type)

restaurant3.describe_restaurant()
restaurant3.open_restaurant()