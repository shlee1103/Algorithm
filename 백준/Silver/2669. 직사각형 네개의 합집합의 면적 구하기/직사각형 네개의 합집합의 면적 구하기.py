recs = 4

total_A = 0
duplicated_cnt = 0

# 좌표범위 100 -> 0으로 채운 빈 리스트 생성
board = [[0] * 100 for _ in range(100)]

for rec in range(recs):

    arr = list(map(int, input().split()))

    for i in range(arr[1], arr[3]):
        for j in range(arr[0], arr[2]):

            # 만약에 해당 자리에 1이 있으면 중복 카운트 + 1
            if board[i][j] >= 1:
                duplicated_cnt += 1

            # 사각형에 해당하는 영역 1로 표시
            board[i][j] += 1

    # 넓이 구하기
    w = arr[2] - arr[0]
    h = arr[3] - arr[1]
    A = w * h
    total_A += A

print(total_A - duplicated_cnt)
