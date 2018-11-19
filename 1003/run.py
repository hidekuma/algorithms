# 1003 - fibonacci

#def fibonacci_cnt(n, zero=0, one=0):
#    if n == 0:
#        #print(0)
#        zero+=1
#        return 0, zero, one
#    elif n == 1:
#        #print(1)
#        one+=1
#        return 1, zero, one
#    else:
#        fib1 = fibonacci_cnt(n-1)
#        fib2 = fibonacci_cnt(n-2)
#        zero += fib1[1]+fib2[1]
#        one += fib1[2]+fib2[2]
#        return fib1[0]+fib2[0], zero, one
#
#def fibonacci_pos(n):
#    if n == 0:
#        return 0
#    elif n == 1:
#        return 1
#    else:
#        return test(n-1) + test(n-2) 


fibo_arr = [0, 1]
def fiborun(num):
    if num == 0:
        print('1 0')
    elif num == 1:
        print('0 1')
    else:
        length = len(fibo_arr)
        if length < num+1:
            for i in range(length, num+1):
                fibo_arr.append(fibo_arr[i-1]+fibo_arr[i-2])
                
        print('{} {}'.format(fibo_arr[num-1],fibo_arr[num]))

inp = int(input())
for _ in range(inp):
    n = int(input())
    fiborun(n)
    
    #rtn = fibonacci_cnt(n)
    #print('%s %s' % (rtn[1], rtn[2]))
    #print('-'*30)
