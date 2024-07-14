N, X = input().split()
N = int(N)
X = int(X)
A = list(map(int, input().split()))


for i in A:
    if i < X:
        print(i, end=" ")