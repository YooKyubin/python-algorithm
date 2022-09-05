from collections import deque
import sys

n = int(sys.stdin.readline())

# 그래프 생성
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
  a, b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)
answer = list(map(int, sys.stdin.readline().split()))

# 제출한 답에 따른 bfs탐색 순서 설정
bfs_order =  [0] * (n+1)
for i in range(n):
  bfs_order[answer[i]] = i+1

# 탐색 순서에 맞게 그래프의 노드 순서 정렬
for g in graph:
  g.sort(key = lambda x: bfs_order[x])

# bfs 순서를 반환하는 함수
def bfs():
  result = []
  q = deque()
  visited = [False] * (n+1)
  q.append(1)
  visited[1] = True
  while q:
    v = q.popleft()
    result.append(v)
    for i in graph[v]:
      if not(visited[i]):
        q.append(i)
        visited[i] = True
  return result

# 제출한 답과 탐색 순서에 맞게 bfs를 한 결과 비교
if answer == bfs():
  print(1)
else:
  print(0)
