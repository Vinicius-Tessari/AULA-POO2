class ListaDeTarefas:
    def __init__(self):
        self._tarefas = []
    
    def adicionar(self, tarefa):
        self._tarefas.append(tarefa)
    
    def __len__(self):
        return len(self._tarefas)
    
    def __iter__(self):
        return iter(self._tarefas)
    
    def __getitem__(self, indice):
        return self._tarefas[indice]


tarefas = ListaDeTarefas()
tarefas.adicionar("estudar")
tarefas.adicionar("ir pra academia")

print(f"Total: {len(tarefas)}")

for tarefa in tarefas:
    print(f"- {tarefa}")

print(f"Primeira tarefa: {tarefas[0]}")
