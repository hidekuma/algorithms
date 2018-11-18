# stack - 2504

X = str(input())

chk_brackets = ('(', '[')
stack = []
#print(X)

def loop(IN_X):
    if len(IN_X) > 30:
        return 0
    value = 0
    count = 0
    for x in IN_X:
        if count == 0 and x not in chk_brackets:
            return 0
        if x in chk_brackets:
            stack.append(x)
        else:
            if len(stack) > 0:
                pop_bracket = stack.pop()
                if pop_bracket == '(' and x == ')':
                    stack.append(2)
                elif pop_bracket == '[' and x == ']':
                    stack.append(3)
                else:
                    stack.append(pop_bracket)
                    while True:
                        if len(stack) > 0:
                            v = stack.pop()
                            if isinstance(v, int):
                                value += v
                            else:
                                if v == '(' and x == ')':
                                    value *= 2
                                elif v =='[' and x == ']':
                                    value *= 3
                                else:
                                    return 0
                                stack.append(value)
                                break
                        else:
                            return 0
                    value = 0
        #print(x)
        #print(stack)
        count += 1

    value = 0
    if len(stack) > 0:
        for s in stack:
            if isinstance(s, str):
                return 0
            else:
                value+=s
    return value

print(loop(X))

