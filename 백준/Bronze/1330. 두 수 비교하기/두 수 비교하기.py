A, B = input().split()
A = int(A)
B = int(B)

# A, B = list(map(int, input().split()))


if A > B:
    print(">")
if A < B:
    print("<")
if A == B:
    print("==")