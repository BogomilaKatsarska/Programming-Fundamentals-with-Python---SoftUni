# 4.	Double Char
# You will be given a string. You should print a string in which each character (case-sensitive) is repeated twice.


word = input()
for index in range(len(word)):
    print(word[index]*2, end='')