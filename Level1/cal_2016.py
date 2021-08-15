#2016년
def solution(a, b):
    temp = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    month = [31, 29, 31 ,30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    for i in range(a-1):
        day += month[i]
    return temp[(day + b) % 7] 

print(solution(1, 1))
