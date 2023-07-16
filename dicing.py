# todos = ['Throw trash away', 'Fix ur bikes', 'Git bi kahve al']
todos = []

while True:
    user_action = input('Type: add, show, edit or exit ').strip()

    if 'add' in user_action[:4]:
        # The command goes like: add so slice until you reach add and a space
        todo = user_action[4:] + '\n'
        todos.append(todo)

        # Open and read todos.txt
        with open('todos.txt', 'r') as f:
            todos = f.readlines()

        # Append the todo to that txt
        todos.append(todo)

        # Now write the todos txt you created locally to the txt file
        with open('todos.txt', 'w') as f:
            # todos.strip('\n')
            content = f.writelines(todos)

    elif 'show' in user_action:
        # Read todos txt
        with open('todos.txt', 'r') as f:
            todos = file.readlines()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'[{index + 1 }] -- {item}'
            row.strip('\n')
            print(row)

    elif 'edit' in user_action:
        # The command goes like: edit 2, so slice until you reach 2
        

        # Adjust their number to the python indexing

        #Read todos.txt

        #Ask for the new todo
        #Override the old with the new todo

        #Write the new todo to the todo.txt

    
        #Slice until complete and a space

        # Read todos txt

        # Adjust 'index' to the program

        # Strip the backslash

        # Remove that index

        # Write the edited todos to todos.txt

        #Notify the user
        message = f'Todo {todo_to_remove} was removed from the list'
        print(message)

    elif 'exit' in user_action:
        break
    else:
        print('Not understood') 

print('Bye')