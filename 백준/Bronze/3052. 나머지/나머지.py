n = 10
B = 42

result_list = []

for i in range(1, n + 1):
    A = int(input())
    result = A % B
    result_list.append(result)
    result_set = set(result_list)

print(len(result_set)) 
