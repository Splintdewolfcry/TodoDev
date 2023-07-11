todos = ['Throw trash away', 'Fix ur bikes', 'Git bi kahve al']

while True:
    user_action = input('Type: add, show, edit or exit  ').strip()

    match user_action:
        case 'add':
            todo = input('Enter a to-do: ')
            todos.append(todo)
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f'[{index + 1}] - {item}'
                print(row)
        case 'edit':
            for index, item in enumerate(todos):
                row = f'[{index + 1}] - {item}'
                print(row)

                number = int(input('Number of the todo to edit: '))
                number = number - 1
                new_todo = input('Input new todo')
                todos[number] = new_todo
        case 'complete':
            number = int(input('Which one did you complete?  '))
            todos.pop(number)
        case 'exit':
            break
        case _:
            print('Not understood') 
