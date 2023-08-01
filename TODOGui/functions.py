#Expects a todos.txt in the same folder
FILEPATH = 'todos.txt'


def get_todos(filepath = FILEPATH):
    """ Read a text in file in the path 'FILEPATH'
    and return the said read result to todos_local
    """
    with open(filepath, 'r') as f:
            todos_local = f.readlines()
    return todos_local

def write_todos(todos_arg, filepath = FILEPATH, ):
    """ Takes 2 arguments. Filepath is for the file you want
    to write to and todos_arg shadows the actual todos variable
    we use in this py file. """
    with open(filepath, 'w') as f:
        content = f.writelines(todos_arg)