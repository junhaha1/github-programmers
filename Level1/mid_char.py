#가운데 글자 가져오기
def solution(s):
    i = len(s) // 2
    if len(s) % 2 == 0:
        answer = s[i - 1 : i + 1]
    else:
        answer = s[i]
    return answer

print(solution("abcde"))