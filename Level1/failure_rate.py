def solution(N, stages):
    answer = [i for i in range(1, N + 1)]
    temp = dict(zip(answer, [0] * (N)))
    result =[]
    cnt = 0

    for i in sorted(list(set(stages))):
        if i > N:
            continue
        temp[i] = stages.count(i) / (len(stages) - cnt)
        cnt += stages.count(i)
    temp = sorted(temp.items(), reverse=True)
    temp = dict(sorted(temp, key = lambda x : x[1]))

    for i in temp.keys():
        result.append(i)
    
    result.reverse()

    return result

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
