# 6.	Next Happy Year
# You are saying goodbye to your best friend: "See you next happy year".
# Happy Year is the year with only distinct digits, for example 2018.
# Write a program that receives an integer number and finds the next happy year.


current_year = int(input())

while True:
    current_year +=1
    current_year_as_str = str(current_year)
    if len(current_year_as_str) == len(set(current_year_as_str)):
        print(current_year)
        break