items = [2,2,3,3]	
budget = 10

new = 0
count = 0

for i in sorted(items):
    new += i
    if new > budget:
        break
    count += 1

print(count)