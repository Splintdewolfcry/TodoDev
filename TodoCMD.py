from functions import get_todos, write_todos


while True:
    user_action = input('Type: add, show, edit, exit or complete ').strip()

    if user_action.startswith('add'):
        # The command goes like: add so slice until you reach add and a space
        todo = user_action[4:] + '\n'
        todos.append(todo)

        # Open and read todos.txt
        todos = get_todos('todos.txt')

        # Append the todo to that txt
        todos.append(todo)

        # Now write the todos txt you created locally to the txt file
        write_todos('todos.txt', todos)

    elif user_action.startswith('show'):
        # Read todos txt
        todos = get_todos('todos.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'[{index + 1 }] -- {item}'
            row.strip('\n')
            print(row)

    elif user_action.startswith('edit'):
        # The command goes like: edit 2, so slice until you reach 2
        number = user_action[4:]
        number = int(number)

        # Adjust their number to the python indexing
        number = number - 1
        #Read todos.txt
        todos = get_todos('todos.txt')

        #Ask for the new todo
        #Override the old with the new todo
        new_todo = input('Input the new to-do: ')
        todos[number] = new_todo + '\n'

        #Write the new todo to the todo.txt
        write_todos('todos.txt', todos)

    elif user_action.startswith('complete'):
        #Slice until complete and a space
        number = user_action[9:]
        number = int(number)

        # Adjust 'index' to the program
        number = number - 1        
        
        # Read todos txt
        todos = get_todos('todos.txt')

        # Remove that index
        todo_removed = todos.pop(number).strip('\n')
        print(type(todo_removed))

        # Write the edited todos to todos.txt
        write_todos('todos.txt', todos)

        #Notify the user
        message = f'Todo {todo_removed} was removed from the list'
        print(message.strip('\n'))

    elif 'exit' in user_action:
        break
    else:
        print('Not understood') 

print('Bye')