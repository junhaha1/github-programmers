def solution(new_id):
    
    answer = ''

    str_list1 = [chr(i) for i in range(97, 123)]
    str_list2 = ['-', '_', '.']
    str_list3 = [str(i) for i in range(10)]
    
    #1번째
    answer = new_id.lower()

    #2번째
    temp1 = ''
    for i in answer:
        if (i in str_list1) or (i in str_list2) or (i in str_list3):
            temp1 += i

    #3번째 
    temp = ''
    temp2 = ''
    for i in temp1:
        if temp2 == '.' and i == '.':
            temp2 = i
            continue
        temp += i
        temp2 = i
    
    #4번째 
    if temp[0] == '.':
        temp = temp[1:]
    elif temp[-1] == '.':
        temp = temp[0:-1]
    elif temp[0] == '.' and temp[-1] == '.':
        temp = temp[1:-1]

    #5단계
    if temp == '':
        temp += 'a'

    #6단계
    if len(temp) > 15:
        temp = temp[0:15]

    if temp[-1] == '.':
        temp = temp[0:-1]

    #7단계
    if len(temp) < 3:
        while True:
            temp += temp[-1]
            if len(temp) >= 3:
                break
    return temp

print(solution("abcdefghijklmn.p"))
