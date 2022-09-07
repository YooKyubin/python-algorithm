from collections import deque
from sys import stdin

n = int(stdin.readline())
graph = [list(map(int, stdin.readline().split())) for _ in range(n)]
island_id = [[0] * n for i in range(n)] # 섬의 위치에 해당 섬 id를 저장하는 지도, 바다는 0
dist = [[-1] * n for _ in range(n)] # bfs로 섬마다 거리를 표현, 거리를 아직 모르는 바다는 -1

# 하나의 노드에 대해 4방향중 범위를 벗어나지 않는 노드들을 list로 반환하는 함수
def check_boundary(y, x):
  _list = []
  dx = [1, -1 ,0, 0]
  dy = [0, 0, 1, -1]
  for d in range(4):
    j = x+dx[d]
    i = y+dy[d]
    if 0 <= i < n and 0 <= j < n:
      _list.append((i,j))
  return _list

# 섬의 개수를 세고 섬의 위치에 섬 id를 저장하는 함수
def bfs(y, x, island_cnt):
  q = deque()
  q.append((y,x))
  graph[y][x] = 0
  island_id[y][x] = island_cnt
  dist[y][x] = 0
  while q:
    y, x = q.popleft()
    for i, j in check_boundary(y, x):
      if graph[i][j] == 1:
        q.append((i,j))
        graph[i][j] = 0 # 확인한 섬위치는 0으로 변경
        island_id[i][j] = island_cnt # 섬이 있는 위치에 id 저장
        dist[i][j] = 0 # 섬은 거리가 0

# 그래프 전체를 돌며 bfs() 호출, 섬위치 파악
island_cnt = 1
for i in range(n):
  for j in range(n):
    if graph[i][j] != 0:
      bfs(i, j, island_cnt)
      island_cnt += 1


# 거리 계산을 위한 bfs
# 섬을 전부 큐에 넣어 bfs시작
que = deque()
for i in range(n):
  for j in range(n):
    if dist[i][j] == 0:
      que.append((i,j))

bridge_len = 200 # n < 100이기 때문에 200보다 큰 거리가 나오지 않음
while que:
  y, x = que.popleft()
  for i, j in check_boundary(y, x):
    if dist[i][j] == -1:
      que.append((i,j))
      dist[i][j] = dist[y][x] + 1
      # 해당 위치가 어떤 섬으로부터의 거리인지 알기 위해 id를 저장
      island_id[i][j] = island_id[y][x]
    else:
      # id가 서로 다르다면 서로 다른 섬으로부터의 거리이기때문에 두 거리를 더하면 다리의 길이가 계산됨
      if island_id[i][j] != island_id[y][x]:
        # 가장 짧은 거리계산
        bridge_len = min(dist[i][j] + dist[y][x], bridge_len)
        
print("island_id")
print(*island_id, sep='\n')
print("dist")
print(*dist, sep='\n')
print(f"{bridge_len=}")
