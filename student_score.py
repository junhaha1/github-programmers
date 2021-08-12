def solution(scores):
    temp = []
    answer = ''

    #각자 자기 자신의 점수 모음
    for i in range(len(scores)): 
        temp.append(scores[i][i])
    
    for i in range(len(scores)):
        temp2 = 0
        count = 0
        char = ''
        for j in range(len(scores)):
            if j == i and (scores[j][i] == max(temp) or scores[j][i] == min(temp)):
                continue
            temp2 += scores[j][i]
            count += 1
        avg = temp2 / count

        if avg >= 90:
            char = "A"
        elif 80<= avg < 90:
            char = "B"
        elif 70<= avg < 80:
            char = "C"
        elif 50<= avg < 70:
            char = "D"
        else:
            char = "F"
        
        answer += char
            
    return answer

print(solution([[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]))