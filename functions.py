# todos = ['Throw trash away', 'Fix ur bikes', 'Git bi kahve al']
# todos = []

def get_todos():
    with open('todos.txt', 'r') as f:
            todos_local = f.readlines()
    return todos_local


while True:
    user_action = input('Type: add, show, edit, exit or complete ').strip()

    if user_action.startswith('add'):
        # The command goes like: add so slice until you reach add and a space
        todo = user_action[4:] + '\n'
        todos.append(todo)

        # Open and read todos.txt
        todos = get_todos()

        # Append the todo to that txt
        todos.append(todo)

        # Now write the todos txt you created locally to the txt file
        with open('todos.txt', 'w') as f:
            # todos.strip('\n')
            content = f.writelines(todos)

    elif user_action.startswith('show'):
        # Read todos txt
        todos = get_todos()

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
        todos = get_todos()

        #Ask for the new todo
        #Override the old with the new todo
        new_todo = input('Input the new to-do: ')
        todos[number] = new_todo + '\n'

        #Write the new todo to the todo.txt
        with open('todos.txt', 'w') as f:
            todos = f.writelines(todos)

    elif user_action.startswith('complete'):
        #Slice until complete and a space
        number = user_action[9:]
        number = int(number)

        # Adjust 'index' to the program
        number = number - 1        
        
        # Read todos txt
        todos = get_todos()

        # Remove that index
        todo_removed = todos.pop(number)
        print(type(todo_removed))

        # Write the edited todos to todos.txt
        with open('todos.txt', 'w') as f:
            todos = f.writelines(todos)

        #Notify the user
        message = f'Todo {todo_removed} was removed from the list'
        print(message.strip('\n'))

    elif 'exit' in user_action:
        break
    else:
        print('Not understood') 

print('Bye')