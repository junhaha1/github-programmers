def solution(scores):
    temp = []
    count = 0
    answer = ''

    #각자 자기 자신의 점수 모음
    for i in scores: 
        temp.append(i[count])
        count += 1

    count = 0
    
    #평균 구하기
    for i in scores:
        if i[count] == max(temp):
            i.remove(max(temp))
        elif i[count] == min(temp):
            i.remove(min(temp))
        count += 1

        print(i)

        avg = sum(i) / len(i)
        char = ''
        if avg >= 90:
            char = 'A'
        elif avg >= 80 and avg < 90:
            char = 'B'
        elif avg >= 70 and avg < 80:
            char = 'C'
        elif avg >= 50 and avg < 70:
            char = 'D'
        else:
            char = 'F'
        answer += char

    return answer

print(solution([[50,90],[50,87]]))