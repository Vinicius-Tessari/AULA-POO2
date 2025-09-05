class ToDoList:
    def __init__(self):
        self._tasks = []

    def add(self, task: str):
        self._tasks.append(task)

    def __len__(self):
        return len(self._tasks)
    
    def __getitem__(self, index): # Acessar usando colchetes
        return self._tasks[index]
    
    def __iter__(self): # Permitir ser usado em loops
        return iter(self._tasks)
    
list = ToDoList()
list.add("Codar")
list.add("Dormir")

print(len(list))

for task in list:
    print("-", task)

print(list[0])