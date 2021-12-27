# 1.	Invert Values
# Write a program that receives a single string containing positive and negative
# numbers separated by a single space. Print a list containing the opposite of each number.

numbers_str = input().split()
numbers_inverted = []

for number in numbers_str:
    number_inverted = int(number) * -1

    numbers_inverted.append(number_inverted)
print(numbers_inverted)

