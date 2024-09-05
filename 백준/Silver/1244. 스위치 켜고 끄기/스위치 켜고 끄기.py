N = int(input())
arr = list(map(int, input().split()))
student_num = int(input())

for _ in range(student_num):
    gender, num = map(int, input().split())

    # gender가 남자인 경우
    if gender == 1:
        for i in range(1, N+1):
            if 0 <= num*i - 1 < N:
                if arr[num * i - 1] == 0:
                    arr[num * i - 1] = 1
                else:
                    arr[num * i - 1] = 0
            else:
                break

    # gender가 여자인 경우
    elif gender == 2:
        # center idx는 무조건 바뀜
        center_idx = num - 1
        if arr[center_idx] == 0:
            arr[center_idx] = 1
        else:
            arr[center_idx] = 0

        # 좌, 우 숫자들 처리 -> 대칭되는 게 같지 않은 경우 나오면 break + 범위 지정
        i = 1
        while True:
            left_idx = center_idx - i
            right_idx = center_idx + i

            if 0 <= left_idx < N and 0 <= right_idx < N:
                if arr[left_idx] != arr[right_idx]:
                    break

                if arr[left_idx] == arr[right_idx] == 1:
                    arr[left_idx] = 0
                    arr[right_idx] = 0
                elif arr[left_idx] == arr[right_idx] == 0:
                    arr[left_idx] = 1
                    arr[right_idx] = 1
            else:
                break

            i += 1

for i in range(0, len(arr), 20):
    print(*arr[i:i + 20])