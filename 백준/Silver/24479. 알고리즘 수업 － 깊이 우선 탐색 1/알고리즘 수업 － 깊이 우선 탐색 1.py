import sys
sys.setrecursionlimit(10**6)  # 재귀 제한 늘리기
input = sys.stdin.readline  # 빠른 입력

def dfs(v):
    global order
    visited[v] = order
    order += 1
    for i in sorted(graph[v]):  # 인접 정점을 오름차순으로 방문
        if visited[i] == 0:
            dfs(i)

# 입력 받기
N, M, R = map(int, input().split())

# 그래프 초기화 (인접 리스트 사용)
graph = [[] for _ in range(N+1)]

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문 순서를 저장할 리스트
visited = [0] * (N+1)

# 방문 순서
order = 1

# DFS 수행
dfs(R)

# 결과 출력
for i in range(1, N+1):
    print(visited[i])