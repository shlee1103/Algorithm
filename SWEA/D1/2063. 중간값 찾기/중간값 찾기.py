score_num = int(input())
score_list = list(map(int, input().split()))

sorted_score_list = sorted(score_list)
print(sorted_score_list[(score_num-1) // 2])
print(sorted_score_list)
