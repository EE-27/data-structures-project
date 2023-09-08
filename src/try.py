stack = []


def push(data):
    stack.append(data)


push("A")
push("B")
push("C")

for index, el in enumerate(stack, 1):
    print(index, "-", el)
