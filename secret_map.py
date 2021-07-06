#2인수 변환 함수
def binary(arr):
    result = []
    for i in arr:
        temp = []
        while i >= 1:
            temp.append(i % 2)
            i = i // 2
        if len(temp) < 5:
            temp.append(0)
        temp.reverse()
        result.append(temp)
    return result

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = ''
        arr1[i] = format(arr1[i], 'b').zfill(n)
        arr2[i] = format(arr2[i], 'b').zfill(n)

        for x, y in zip(arr1[i], arr2[i]):
            if int(x) or int(y):
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
