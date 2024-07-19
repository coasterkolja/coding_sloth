from stack import Stack

queue = ["MyStack", [1], [2], "top", "pop", "empty"]

for cmd in queue:
    if cmd == "MyStack":
        myStack = Stack()
    elif cmd == "top":
        print(myStack.top())
    elif cmd == "pop":
        print(myStack.pop())
    elif cmd == "empty":
        print(myStack.isEmpty())
    else:
        myStack.push(cmd)