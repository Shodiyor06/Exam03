class TodoList:
    def __init__(self):
        self.lst = []
    def add_task(self):
        task = input("task:")
        self.lst.append(task)
    def show_task(self):
        return self.lst
todo = TodoList()
while True:
    
    todo.add_task()
    todo.add_task()
    print(todo.show_task())

    