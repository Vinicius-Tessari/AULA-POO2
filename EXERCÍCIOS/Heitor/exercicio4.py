from abc import ABC, abstractmethod

class Forma(ABC):
    @abstractmethod
    def area(self):
        pass

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2


quadrado = Quadrado(25)
print(f"Área do quadrado: {quadrado.area()}")
