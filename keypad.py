def solution(numbers, hand):
    answer = ''
    keyboard = [[1,2,3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    
    left = [0, 3]
    right = [2, 3]

    for i in numbers:
        print(i)
    
    return answer


solution([1,2,3,4], "right")