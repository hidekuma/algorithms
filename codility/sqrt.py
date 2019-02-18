def solution(A, B):

    result = None
    def sqrt(input, loop_count=0):
        # -- 루트
        rtn = input ** 0.5
        # -- 소수점 체크
        #print('test1', rtn)
        if rtn % 1 == 0:
            if loop_count > 0:
                nonlocal result
                result = rtn
            loop_count += 1
            return sqrt(rtn, loop_count)

    for n in range(A,B+1):
        sqrt(n, 0)
    #print(result)
    return int(result)




solution(6000,7000)
