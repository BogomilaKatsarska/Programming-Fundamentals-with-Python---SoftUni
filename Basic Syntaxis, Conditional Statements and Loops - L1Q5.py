# 5.	Patterns
# Write a program which receives a number and creates the following pattern. The number represents the largest count of stars on one row.


num = int(input())

for n in range(num+1):
    print("*"*n)
for n in range(num-1, 0, -1):
    print("*" * n)