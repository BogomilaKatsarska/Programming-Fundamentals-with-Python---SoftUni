# You will receive a single number n. On the next n lines you will receive integers. After that you will be given one of the following commands:
# •	even
# •	odd
# •	negative
# •	positive
# Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.

n = int(input())
even = []
odd = []
negative = []
positive = []

for _ in range(n):
    num = int(input())
    if num < 0:
        negative.append(num)
    if num >= 0:
        positive.append(num)
    if num % 2 == 0:
        even.append(num)
    if not num % 2 == 0:
        odd.append(num)

command = input()
if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "negative":
    print(negative)
else:
    print(positive)
