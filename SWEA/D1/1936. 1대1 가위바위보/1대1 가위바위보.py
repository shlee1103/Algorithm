Scissors = '1'
Rock = '2'
Paper = '3'

A, B = input().split()

if (A == Scissors and B == Paper) or (A == Rock and B == Scissors) or (A == Paper and B == Rock):
    print("A")
else:
    print("B")