todos = []

while True:
    user_choice = input("add, show or exit")

    match user_choice:
        case 'add':
            todo = input('Enter a to-do: ')
            todos.append(todo)
