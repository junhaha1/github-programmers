def solution(numbers, hand):
    answer = ''
    keyboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    
    left = [[3, 0]]
    right = [[3, 2]]

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
            left_p = abs(left[0][0] - temp_position[0][0]) + abs(left[0][1] - temp_position[0][1])
            right_p = abs(right[0][0] - temp_position[0][0]) + abs(right[0][1] - temp_position[0][1])
            if left_p > right_p:
                right = list(temp_position)
                answer += 'R'
            elif left_p < right_p:
                left = list(temp_position)
                answer += 'L'
            else:
                if hand == "right":
                    right = list(temp_position)
                elif hand == "left":
                    left = list(temp_position)
                answer += hand[0].upper()
    return answer