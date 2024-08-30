# 입력받기
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

w_compare_cnt = 9999999
b_compare_cnt = 99999999

for x in range(N - 8 + 1):
    for y in range(M - 8 + 1):

        w_s_cnt = 0
        b_s_cnt = 0

        for i in range(8):
            for j in range(8):
                # 좌상단 white 행탐색
                if i % 2 == 0 and j % 2 == 0:
                    if arr[x+i][y+j] != 'W':
                        w_s_cnt += 1
                elif i % 2 == 1 and j % 2 == 1:
                    if arr[x+i][y+j] != 'W':
                        w_s_cnt += 1
                else:
                    if arr[x+i][y+j] != 'B':
                        w_s_cnt += 1

                # 좌상단 black 행탐색
                if i % 2 == 0 and j % 2 == 0:
                    if arr[x+i][y+j] != 'B':
                        b_s_cnt += 1
                elif i % 2 == 1 and j % 2 == 1:
                    if arr[x+i][y+j] != 'B':
                        b_s_cnt += 1
                else:
                    if arr[x+i][y+j] != 'W':
                        b_s_cnt += 1

        if w_compare_cnt > w_s_cnt:
            w_compare_cnt = w_s_cnt

        if b_compare_cnt > b_s_cnt:
            b_compare_cnt = b_s_cnt

print(min(w_compare_cnt, b_compare_cnt))
