
student = int(input())
num = list(map(int, input().split()))

student_arr = [i for i in range(1, student+1)]
seat = []


for i in student_arr:
    for j in range(i):
        if num[i-1] == j:
            seat.insert(i-1-j, i)
            # seat[i-1-j] = student_arr[j]

print(*seat)


