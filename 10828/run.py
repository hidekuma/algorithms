n = int(input())

stack = []
for i in range(n):
    inp = input().split()
    if len(inp) >= 2:
        if inp[0] == 'push':
            stack.append(inp[1])
    else:
        if inp[0] == 'pop':
            if len(stack) == 0:
                print(-1)
            else:
                pop = stack.pop()
                print(pop)
        elif inp[0] == 'size':
            print(len(stack))
        elif inp[0] == 'empty':
            if len(stack) == 0:
                print(1)
            else:
                print(0)
        elif inp[0] == 'top':
            if len(stack) == 0:
                print(-1)
            else:
                print(stack[len(stack)-1])
