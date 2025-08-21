from abc import ABC, abstractmethod
from datetime import date, timedelta

class ItemBiblioteca(ABC):
    """Classe abstrata base para todos os itens da biblioteca"""
    
    def __init__(self, codigo: str, titulo: str, ano: int, estoque: int = 1):
        self.codigo = codigo
        self.titulo = titulo
        self.ano = ano
        self.estoque = estoque
    
    @abstractmethod
    def dias_de_emprestimo(self) -> int:
        """Retorna o número de dias que o item pode ser emprestado"""
        pass
    
    @abstractmethod
    def get_tipo(self) -> str:
        """Retorna o tipo do item"""
        pass
    
    def __str__(self) -> str:
        return f"{self.get_tipo().title()}('{self.titulo}', {self.ano})"

class Livro(ItemBiblioteca):
    """Representa um livro na biblioteca"""
    
    def dias_de_emprestimo(self) -> int:
        return 14
    
    def get_tipo(self) -> str:
        return "livro"

class Revista(ItemBiblioteca):
    """Representa uma revista na biblioteca"""
    
    def dias_de_emprestimo(self) -> int:
        return 7  # Revistas têm prazo menor de empréstimo
    
    def get_tipo(self) -> str:
        return "revista"