todos = ['Throw trash away', 'Fix ur bikes', 'Git bi kahve al']

while True:
    user_action = input('Type: add, show, edit or exit ').strip()

    if 'add' in user_action[:4]:
        # The command goes like: add so slice until you reach add and a space
        todo = user_action[4:]
        todos.append(todo)

        # Open and read todos.txt

        # Append the todo to that txt

        # Now write the todos txt you created locally to the txt file


    elif 'show' in user_action:
        # Read todos txt

        for index, item in enumerate(todos):
            # item = item.strip('\n')
            row = f'[{index + 1 }] -- {item}'
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