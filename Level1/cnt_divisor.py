def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        temp =[1]
        for j in range(2, i + 1):
            if i % j == 0:
                temp.append(j)
        if len(temp) % 2 == 0:
            answer += temp[-1]
        else:
            answer -= temp[-1]
    return answer