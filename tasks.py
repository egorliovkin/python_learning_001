# n, t = map(int, input().split())
# tasks = [(x+1)*5 for x in range(n)]
# limit = 240 - t
# n = 0
# for x in tasks:
#     if x <= limit:
#         limit -= x
#         n += 1
#     else:
#         break
# print(n)

n, t = map(int, input().split())
tasks = [(x+1)*5 for x in range(n)]
limit = 240 - t
n = 0
while n < len(tasks) and tasks[n] <= limit:
        limit -= tasks[n]
        n += 1
print(n)