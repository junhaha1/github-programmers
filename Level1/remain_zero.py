#나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    
    for i in arr.copy():
        if i % divisor != 0:
            arr.remove(i)

    if not arr: 
        arr.append(-1)

    return sorted(arr)

print(solution([3,2,6], 5))