croatia_str = ['c=', 'c-', 'dz=', 'd-',
               'lj', 'nj', 's=', 'z=']

word = input()

for alphabet in croatia_str:
    word = word.replace(alphabet, '*')

print(len(word))
