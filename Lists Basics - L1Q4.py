# 4.	Search
# You will receive a number n and a word.
# On the next n lines you will be given some strings.
# You should add them in a list and print them.
# After that you should filter out only the strings that include the given word and print that list too.


n = int(input())
word = input()
list_one = []
list_two = []

for _ in range(n):
    some_string = input()
    list_one.append(some_string)
    if word in some_string:
        list_two.append(some_string)

print(list_one)
print(list_two)