from collections import deque

d = deque()

print(d)

for i in range(10):
    d.append(i)

print(d)

d = deque(range(20))
print(d)

d.appendleft(100)
print(d)

d.extendleft([56, 87])

print(d)

d.insert(10, 90)
print(d)

d.pop()
print(d)
