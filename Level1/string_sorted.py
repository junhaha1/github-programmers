def solution(strings, n):
    temp = sorted(strings)
    return sorted(temp, key = lambda x : x[n])