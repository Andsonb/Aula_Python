def undo(todo_list, redo_list):
    if not todo_list:
        print('nada a fazer')
        return
    last_todo = todo_list.pop()
    redo_list.append(last_todo)


def redo(todo_list, redo_list):
    if not redo_list:
        print('nada a fazer')
        return
    last_redo = redo_list.pop()
    todo_list.append(last_redo)


def do_add(todo, todo_list):
    todo_list.append(todo)


def show_op(todo_list):
    print()
    print('tarefas')
    print(todo_list)
    print()


if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('digite uma tarefa, undo, redo, ls: ')
        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            redo(todo_list, redo_list)
            continue
        do_add(todo, todo_list)
