FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    '''load list from filepath (default is todos.txt) and assigns to list todos'''
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath=FILEPATH):
    '''open file and write todos to filepath (default is todos.txt)'''
    with open(filepath, 'w') as file:
        file.writelines(todos)


def show_list():
    '''calls get_todos function then show the list in a numbered column'''
    print("Your list of todos: ")
    todos = get_todos()
    for index, item in enumerate(todos):
        item = item.strip('\n')
        row = f"{index + 1}) {item}"
        print(row)


# this is so that the program 'cli_main.py' does not run the following
# if the following is run from functions.py, it will output '__main__'
# if the following is run from outside of functions.py (for example from
#  'cli_main.py', it will output 'functions'
#print(__name__)
if __name__ == '__main__':
    print("hello")
    print(show_list())