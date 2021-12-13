# 2.	Number Definer
# Write a program that reads a floating-point number and prints "zero" if the number is zero. Otherwise, it should print "positive" or "negative". The program should add "small" if the absolute value of the number is less than 1, or "large" if it exceeds 1 000 000.
#

num = float(input())

if num < -1000000:
    print("large negative")
elif -1000000 <= num <= -1:
    print("negative")
elif -1 < num < 0:
    print("small negative")
elif num == 0:
    print("zero")
elif 0 < num < 1:
    print("small positive")
elif 1 <= num <= 1000000:
    print("positive")
else:
    print("large positive")