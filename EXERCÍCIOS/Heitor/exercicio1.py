class Livro:
    def __init__(self, estoque=0):
        self._estoque = estoque
    
    @property
    def estoque(self):
        return self._estoque
    
    @estoque.setter
    def estoque(self, valor):
        if valor < 0:
            print ("Estoque não pode ser negativo")
        self._estoque = valor

livro = Livro(5)
print(f"estoque: {livro.estoque}")

livro.estoque = 10
print(f"novo estoque: {livro.estoque}")

try:
    livro.estoque = -3
except ValueError as e:
    print(f"Erro: {e}")
