# You will receive a single number n. On the next n lines you will receive names of courses.
# You should create a list of courses and print it.

n = int(input())
list = []

for _ in range(n):
    element = input()
    list.append(element)

print(list)
