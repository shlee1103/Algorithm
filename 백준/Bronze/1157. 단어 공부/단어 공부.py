# upper()  : 입력 받은 문자열을 대문자로
word = input().upper()
word_list = list(set(word)) 
alpha_count = []

for i in word_list: 
    count = word.count(i) 
    alpha_count.append(count) 

if alpha_count.count(max(alpha_count)) >= 2: 
    print('?')
else:
    print(word_list[alpha_count.index(max(alpha_count))])