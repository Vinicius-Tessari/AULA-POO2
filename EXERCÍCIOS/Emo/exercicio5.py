class OpenClose:
    def __init__(self, file: str):
        self.file = file

    def __enter__(self):
        self.f = open(self.file, "a", encoding="utf-8")
        self.f.write("1\n")
        return self.f
    
    def __exit__(self):
        self.f.write("3\n")
        self.f.close()

with OpenClose("abu.txt") as f:
    f.write("2\n")