def show_op(todo_list):
    print()
    print('Lista de Tarefas')
    print(todo_list)
    print()

def do_add(todo, todo_list):
    todo_list.append(todo)

def do_undo(todo_list, redo_list):
    if not todo_list:
        print('Não há nada para DESFAZER.')
        return

    last_undo = todo_list.pop()
    redo_list.append(last_undo)

def do_redo(todo_list, redo_list):
    if not redo_list:
        print('Não há nada para REFAZER.')
        return

    last_redo = redo_list.pop()
    todo_list.append(last_redo)

if __name__ == '__main__':
    todo_list = []
    redo_list = []

    while True:
        todo = input('Adicione item, UNDO, REDO ou ls: ')

        if todo == 'ls':
            show_op(todo_list)
            continue
        elif todo == 'undo':
            do_undo(todo_list, redo_list)
            continue
        elif todo == 'redo':
            do_redo(todo_list, redo_list)
            continue

        do_add(todo, todo_list)


