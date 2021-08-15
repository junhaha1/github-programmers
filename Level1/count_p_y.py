def solution(s):
    cnt1 = 0
    cnt2 = 0

    for i in s.upper():
        if i == "P":
            cnt1 += 1
        elif i == "Y":
            cnt2 += 1

    return cnt1 == cnt2