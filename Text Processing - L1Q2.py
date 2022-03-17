data = input().split()
new_string = ""

for el in data:
    length = len(el)
    new_string += el*length

print(new_string)