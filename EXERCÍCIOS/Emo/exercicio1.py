class Book:
    def __init__(self, title: str, stock: int):
        self.title = title
        self._stock = stock

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if value < 0:
            raise ValueError("Pode numero negativo nao paezao")
        self._stock = value

book = Book("O diario de um abacate", 10)
print(book.stock)
book.stock = 5
print(book.stock)
book.stock = -3