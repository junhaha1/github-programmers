def solution(new_id):

    answer = ''

    str_list1 = [chr(i) for i in range(97, 123)]
    str_list2 = ['-', '_', '.']
    str_list3 = [str(i) for i in range(10)]
    
    #1번째
    new_id = new_id.lower()

    #2번째
    for i in new_id:
        if (i in str_list1) or (i in str_list2) or (i in str_list3):
            answer += i

    #3번째 
    while '..' in answer:
        answer.replace('..', '.')
    
    #4번째 
    if answer[0] == '.':
        if len(answer) > 1:
            answer = answer[1:]
        else:
            answer ='.'
    if answer[-1] == '.':
        answer = answer[:-1]

    #5단계
    if answer == '':
        answer += 'a'

    #6단계
    if len(answer) > 15:
        answer = answer[:15]

    if answer[-1] == '.':
        answer = answer[0:-1]

    #7단계
    while len(answer) < 3:
        answer += answer[-1]

    return answer

print(solution("abcdefghijklmn.p"))
