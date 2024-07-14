# Input two numbers as strings
A, B = input().split()

# Reverse the digits of each number and convert back to integers
reversed_A = int(A[::-1])
reversed_B = int(B[::-1])

# Find the maximum of the two reversed numbers
max_value = max(reversed_A, reversed_B)

# Print the maximum reversed number
print(max_value)
