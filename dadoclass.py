import random

# Definizione della classe Dado

class Dado:
    def __init__(self, lati: int):
        self.lati = lati

    def roll_die(self):
        return random.randint(1, self.lati)

# Funzione per lanciare un dado più volte

def lancia_dado(dado, num_lanci=10):
    print(f"\nLanci del dado a {dado.lati} facce:")
    for i in range(num_lanci):
        risultato = dado.roll_die()
        print(f"Lancio {i+1}: {risultato}")
        
# creazione dei dadi

dado1 = Dado(6)
dado2 = Dado(10)
dado3 = Dado(20)

# Lanci dei dadi

lancia_dado(dado1)
lancia_dado(dado2)
lancia_dado(dado3)
