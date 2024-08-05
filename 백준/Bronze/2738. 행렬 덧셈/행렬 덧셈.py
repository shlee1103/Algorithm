N, M = input().split()
N = int(N)
M = int(M)


A_arr = [list(map(int, input().split())) for _ in range(N)]
B_arr = [list(map(int, input().split())) for _ in range(N, N+N)]

sum_arr = []

for i in range(N):
    new_arr = []
    for j in range(M):
        new_arr.append(A_arr[i][j] + B_arr[i][j])
    sum_arr.append(new_arr)

for i in range(N):
    for j in range(M):
        print(sum_arr[i][j], end = ' ')
    print()

