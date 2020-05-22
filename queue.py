from collections import deque

q = deque(["pete", "craig","Mike"])
print (q)
q.append("john")
print(q)
q.append("james")
print(q)
q.popleft()
print(q)
