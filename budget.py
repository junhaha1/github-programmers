def solution(d, budget):
    answer = 0
    if sum(d) > budget:
        temp = 0

        for i in sorted(d):
            temp += i
            if temp > budget:
                break
            answer += 1
            

    elif sum(d) <= budget:
        answer = len(d)
    
    return answer

#itertools 에서 combinations를 이용하면 시간복잡도가 심각해짐. 
#그래서 조합을 이용하지 않고 풀기