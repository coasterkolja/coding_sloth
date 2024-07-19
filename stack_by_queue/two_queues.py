from stack import Stack

commands = ["MyStack", "push", "push", "top", "pop", "empty"]
items = [[], [1], [2], [], [], []]

for i in range(len(commands)):
    if commands[i] == "MyStack":
        myStack = Stack()
    elif commands[i] == "push":
        myStack.push(items[i])
    elif commands[i] == "top":
        print(myStack.top())
    elif commands[i] == "pop":
        print(myStack.pop())
    elif commands[i] == "empty":
        print(myStack.isEmpty())