#3진법 뒤집기
def solution(n):
    answer = []
    result = 0
    j = 0

    #3진법 전환하여 뒤집어서 리스트에 넣음
    while n > 0:
        answer.append(n % 3)
        n = n // 3
    
    for i in reversed(answer):
        result += i * (3 ** j)
        j += 1
        
    return result

print(solution(45))