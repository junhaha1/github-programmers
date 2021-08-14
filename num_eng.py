def solution(s):
    number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, j in enumerate(number):
        s = s.replace(j, str(i))
    return s