todos = {}

while True:
    print("1.Add 2.Show")
    c = input("> ")

    user = input("User: ")

    if user not in todos:
        todos[user] = []

    if c == "1":
        task = input("Task: ")
        todos[user].append(task)

    if c == "2":
        print(todos[user])
