from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
in_degree = [0] * (n+1)
for _ in range(m):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  in_degree[b] += 1

answer = []
def topological_sort():
  q = deque()
  for i in range(1, n+1):
    if in_degree[i] == 0:
      q.append(i)
      visited[i] = True
  while q:
    v = q.popleft()
    answer.append(v)
    for i in graph[v]:
      if not(visited[i]):
        in_degree[i] -= 1
        if in_degree[i] == 0:
          q.append(i)
          visited[i] = True
v = []
topological_sort()
print(*answer, sep=' ')
        
