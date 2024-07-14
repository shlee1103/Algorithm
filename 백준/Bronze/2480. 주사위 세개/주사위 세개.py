dice_1, dice_2, dice_3 = list(map(int, input().split()))

if dice_1 == dice_2 == dice_3:
    money = 10000+((dice_1)*1000)
elif (dice_1 == dice_2) or (dice_1 == dice_3):
    money = 1000 + ((dice_1)*100)
elif (dice_2 == dice_3):
    money = 1000 + ((dice_2)*100)
elif dice_1 != dice_2 != dice_3:
    money = max(dice_1, dice_2, dice_3)*100

print(money)