n = int(input())
num = list(map(int, input().split()))

new_avg_list = []
for i in range(n):
    num_max = max(num)
    new_avg_list.append((num[i] / num_max) * 100)

new_avg_sum = sum(new_avg_list)
avg_value = new_avg_sum / n
print(avg_value)
    



