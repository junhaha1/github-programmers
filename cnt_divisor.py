def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer

# 제곱수 성질
# 1. 소인수분해 하였을 때, 각 소인수의 지수가 모두 짝수이다
# 2. 제곱수의 약수의 갯수는 항상 홀수이다. 