def solution(numbers, hand):
    answer = ''
    keyboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    
    left = [0, 3]
    right = [2, 3]

    #좌표상 거리 계산으로 접근
    for i in numbers:
        #좌표값 계산
        temp_position = [(x, y) for x in range(len(keyboard)) for y in range(len(keyboard[0])) if keyboard[x][y] == i]

        if i in [1, 4, 7, '*']:
            left = list(temp_position)
            answer += 'L'
        elif i in  [3, 6, 9, '#']:
            right = list(temp_position)
            answer += 'R'
        elif i in  [2, 5, 8, 0]:
            print(temp_position)
    
    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))