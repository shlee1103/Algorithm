# baekjoon 1316
word_count = int(input())

word_lst = []
for _ in range(word_count):
    word_lst.append(list(input()))
# print(word_lst)

# key: alphabet
# value: index
# ex: {a: 0}
existed_alpha_dict = {}
total_group_word_num = 0

for alpha_lst in word_lst:
    for index , alpha in enumerate(alpha_lst): # [a b c] => (0, a) , (1, b), (2, c)
        # alpha, index
        existed_index = existed_alpha_dict.get(alpha)
        existed_alpha = alpha
        current_index = index
        current_alpha = alpha

        # 딕셔너리에 알파벳이 없는 경우
        if existed_index == None : 
            existed_alpha_dict[current_alpha] = current_index
        # 딕셔너리에 알파벳이 있는 경우
        # 1. 현재 alpha가 연속되는 단어인지(=그룹 단어인지) 체크
        elif existed_index + 1 == current_index:
            existed_alpha_dict[existed_alpha] = current_index
        # 2. 그룹 단어가 아닌 경우로 판명난 경우
        else:
            break


        if (index == len(alpha_lst)-1):
            total_group_word_num += 1
    
    existed_alpha_dict = {}

print(total_group_word_num)