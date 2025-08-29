class Relogio:
    def __init__(self, hora=0, minuto=0):
        self.hora = hora
        self.minuto = minuto
    
    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}"

print("relogio 1:")
relogio = Relogio(14, 33)
print(relogio)

print("relogio 2:")
relogio2 = Relogio(5, 2)
print(relogio2)
