def add_(tarefa, ta):
    ta.append(tarefa)



ta=[]

while True:
    ativ = input('digite sua tarefa: ')

    add_(ativ,ta)
    print(ta)