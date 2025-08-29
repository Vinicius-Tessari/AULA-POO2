class AbreFecha:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
    
    def __enter__(self):
        with open(self.nome_arquivo, 'w') as f:
            f.write("Começo\n")
        return self
    
    def __exit__(self, tipo, valor, traceback):
        with open(self.nome_arquivo, 'a') as f:
            f.write("Fim\n")


with AbreFecha("registro.txt"):
    print("indo ao banheiro")
    print("me limpando")
