input_num = input()
input_num_len = len(input_num)

sum = 0 # 다 더한 결과를 보관하는 수
for num in input_num:
    sum = sum + int(num)
print(sum)