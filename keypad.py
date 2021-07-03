def solution(numbers, hand):
    answer = ''
    keyboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    
    left = [0, 3]
    right = [2, 3]

    for i in numbers:
        if i in [1, 4, 7, '*']:
            answer += 'L'
        elif i in  [3, 6, 9, '#']:
            answer += 'R'
    
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))