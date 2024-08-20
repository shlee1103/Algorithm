N = int(input())

for round in range(N):
    a_input = list(map(int, input().split()))
    a_cnt = a_input[0]
    a_input.remove(a_cnt)

    b_input = list(map(int, input().split()))
    b_cnt = b_input[0]
    b_input.remove(b_cnt)

# A가 이기는 경우
    if a_input.count(4) != b_input.count(4):
        if a_input.count(4) > b_input.count(4):
            print('A')
        elif a_input.count(4) < b_input.count(4):
            print('B')

    elif a_input.count(3) != b_input.count(3):
        if a_input.count(3) > b_input.count(3):
            print('A')
        elif a_input.count(3) < b_input.count(3):
            print('B')

    elif a_input.count(2) != b_input.count(2):
        if a_input.count(2) > b_input.count(2):
            print('A')
        elif a_input.count(2) < b_input.count(2):
            print('B')

    elif a_input.count(1) != b_input.count(1):
        if a_input.count(1) > b_input.count(1):
            print('A')
        elif a_input.count(1) < b_input.count(1):
            print('B')

    else:
        print('D')
