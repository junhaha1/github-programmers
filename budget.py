def solution(d, budget):
    answer = 0
    if sum(d) > budget:
        pass
            

    elif sum(d) <= budget:
        answer = len(d)
    
    return answer

print(solution([2,2,3,3], 10))