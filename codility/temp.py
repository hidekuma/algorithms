def solution(T):

    summer = []
    winter = []
    for n in range(1,len(T)):
        if T[0] < T[n]:
            summer.append(T[n])
        else:
            winter.append(T[n])
    winter.append(T[0])


    print(summer)
    print(winter)
    print()
    return len(winter)





solution([5,-2,3,8,6])
solution([-5, -5, -5, -42, 6, 12])
