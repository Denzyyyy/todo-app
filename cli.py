from function import get_todos, write_todos

while True:
    user_action = input('Type add, or show, edit or exit:')
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos(todos)

        todos.append(todo + '\n')

        write_todos("todos.txt", todos)

    elif user_action.startswith('show'):

        todos = get_todos(todos)

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)

            number = number - 1

            todos = get_todos("todos.txt")

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("command is not valid.")

print("Bye!")
