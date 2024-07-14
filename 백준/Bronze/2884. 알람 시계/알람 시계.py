H, M = map(int, input().split())

time_min = (H*60) + M

# divmod() : 몫과 나머지 한 번에 출력
new_H, newM = divmod((time_min - 45), 60)

if new_H == -1:
    new_H = 23

print(new_H, newM)