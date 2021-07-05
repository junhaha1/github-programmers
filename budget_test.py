from itertools import combinations

items = [1,3,2,5,4]
budget = 10

new = []

if sum(items) > budget:
    for i in range(1, len(items)):
        new = ([i for i in list(combinations(items, i)) if sum(i) <= budget])
        
print(len(new[0]))