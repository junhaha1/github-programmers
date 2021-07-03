def solution(new_id):
    answer = ''
    str_list1 = [chr(i) for i in range(97, 123)]
    str_list2 = ['-', '_', '.']
    
    #1번째
    new_id.lower()

    #2번째
    temp1 = ''
    for i in new_id:
        if (i in str_list1) or (i in str_list2):
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
        pass
        
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
