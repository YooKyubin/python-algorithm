import sys
from collections import deque

# 위상정렬 결과를 answer에 저장, 사이클이 있다면 False, 없다면 True 반환
def topological_sort(matrix, in_degree, answer):
  q = deque()
  for i in range(1,n+1):
    if in_degree[i] == 0:
      q.append(i)
  while q:
    v = q.popleft()
    answer.append(v)
    for i in range(1, n+1):
      if matrix[v][i]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
          q.append(i)

  # 위상정렬이 끝났는데 in_degree의 값이 0이 아닌 수가 있다는 것은 사이클이 있어서 다 방문하지 못함을 의미: 불가능
  for i in in_degree:
    if i != 0:
      return False
  
  return True

t = int(sys.stdin.readline())
for _ in range(t):
  answer = []
  n = int(sys.stdin.readline())
  #인접행렬
  matrix = [[False] * (n+1) for _ in range(n+1)]
  in_degree = [0] * (n+1)
  last_rank = list(map(int, sys.stdin.readline().split()))

  # last_rank에서 자신 보다 뒤 순위인 노드들을 향하는 간선 생성
  for i in range(n):
    for j in range(i+1, n):
      matrix[last_rank[i]][last_rank[j]] = True
      in_degree[last_rank[j]] += 1
  
  m = int(sys.stdin.readline())
  for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # a와 b 순서에 상관없이 두 팀의 순위를 바꿈
    # a가 항상 b 순위를 앞서는 것이 아니고, 이미 순위가 높다면 b가 a보다 순위가 높아지는 것임
    if matrix[a][b]: 
      a, b = b, a
    #a와b의 간선 방향을 바꿈
    matrix[b][a] = False
    matrix[a][b] = True
    in_degree[a] -= 1
    in_degree[b] += 1
    
  if topological_sort(matrix, in_degree, answer):
    print(*answer, sep = ' ')
  else:
    print("IMPOSSIBLE")
