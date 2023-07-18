todos = ['Throw trash away', 'Fix ur bikes', 'Git bi kahve al']

while True:
    user_action = input('Type: add, show, edit or exit  ').strip()

    match user_action:
        case 'add':
            todo = input('Enter a to-do: ') + '\n'

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item.strip('\n')
                row = f'[{index + 1}] - {item}'
                print(row)

        case 'edit':
            #show the items
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
                print('Here is the existing todos', todos)

            for index, item in enumerate(todos):
                item.strip('\n')
                row = f'[{index + 1}] - {item}'
                print(row)
            
            #Ask which one you would like to edit
            user_edit_number = int(input('Number of the todo to edit: '))
            user_edit_number = user_edit_number - 1
            
            #Ask user for the changed input
            overriden_todo = input('Input new todo: ')

            todos[user_edit_number] = overriden_todo

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            
                
            
            
            
            
            
            # for index, item in enumerate(todos):
            #     row = f'[{index + 1}] - {item}'
            #     print(row)
            #     for todo in todos:
            #         number = int(input('Number of the todo to edit: '))
            #         number = number - 1
            #         new_todo = input('Input new todo')
            #         todos[number] = new_todo
        case 'complete':
            number = int(input('Which one did you complete?  '))
            todos.pop(number)
        case 'exit':
            break
        case _:
            print('Not understood') 
