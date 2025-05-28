from persona import Persona
from studente import Studente

# creo un oggetto p della classe Persona
p:Persona= Persona("Niccolò", "Veggian", 23)

# visualizzare le informazioni dell'oggetto p
print(p)

#creare un oggetto studente1 della classe Studente
studente1: Studente= Studente("Mario", "Rossi", 20, "0123456")

#visualizzare le informazioni relative all'oggetto studente1
print(studente1)

#controllare se studente1 è istanza della classe Studente
# isistance(obj, Class) -> controlla se l'oggetto obj sia istanza della classe Classe
# in caso affermativo -> True
# in caso negativo -> False
if isinstance(studente1, Studente):
    print("\nstudente1 è istanza della classe Studente")

# controllo se studente1 è un'istanza della classe Persona
if isinstance(studente1, Persona):
    print("\nstudente1 è un oggetto della classe Studente ma è anche oggetto della classe Persona")

# controllo se l'oogetto p sia un'stanza della classe Persona
if isinstance(p, Persona):
    print("\np è un oggetto della classe Persona")
#controllare se l'oggetto p sia anche un'istanza della classe Studente
if isinstance(p, Studente):
    print("\np è un oggetto della classe Persona ma anche della classe Studente")
else:
    print("\np è un oggeto della classe Persona ma non della classe Studente")

# controllare se una Classe è sottoclasse di un'altra
# controllo che la classe Studente sia sottoclasse della classe Persona
# issubclas(Class1, Class2) -> controlla se la classe Class1 è sottoclasse della Class2
# in caso affermativo -> True
# in caso negativp -> False

if issubclass(Studente, Persona):
    print("\nla classe Studente è una sottoclasse della classe Persona")