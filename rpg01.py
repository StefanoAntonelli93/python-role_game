# classe astratta PERSONAGGIO
# importo abstract base method
from abc import ABC, abstractmethod
class Personaggio(ABC):
    def __init__(self, name):
        self.name = name
    # decoratore @abstractmethod
    @abstractmethod
    def attacca(self):
        pass
    def difende(self):
        pass

# classi dei personaggi

class Guerriero(Personaggio):
    def attacca(self):
        return f"{self.name} attacca furiosamente con la spada"
    
class Mago(Personaggio):
    def attacca(self):
        return f"{self.name} lancia potenti incantesimi offensivi"
    
class Ladro(Personaggio):
    def attacca(self):
        return f"{self.name} attacca furtivamente con il suo pugnale"
    
class Chierico(Personaggio):
    def attacca(self):
        return f"{self.name} utilizza un attacco sacro"
    
    def difende(self):
        return f"{self.name} cura i suoi alleati"
    

# creo istanze personaggi
#  se lo script è stato lanciato come programma principale
if __name__ == "__main__":
    aragorn = Guerriero("Aragorn")
    gandalf = Mago("Gandalf")
    bilbo = Ladro("Bilbo")
    sauron = Chierico("Sauron")

    print(aragorn.attacca())
    print(gandalf.attacca())
    print(bilbo.attacca())
    print(sauron.attacca())
    print(sauron.difende())