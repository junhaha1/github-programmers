def solution(scores):
    temp = []
    answer = ''
    count = 0

    #각자 자기 자신의 점수 모음
    for i in range(len(scores)): 
        temp2 = []
        for j in  range(len(scores)):
            temp2.append(scores[j][i])
        temp.append(temp2)
    
    for i in range(len(temp)):
        if temp[i].count(max(temp[i])) == 1 and scores[i][i] == max(temp[i]):
            temp[i].remove(max(temp[i]))
        elif temp[i].count(min(temp[i])) == 1 and scores[i][i] == min(temp[i]):
            temp[i].remove(min(temp[i]))
        
        avg = sum(temp[i]) / len(temp[i])

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