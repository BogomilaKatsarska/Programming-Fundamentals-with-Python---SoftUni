stock = input().split()
keys_and_values = {}

for el in range(0, len(stock), 2):
    key = stock[el]
    value = stock[el+1]
    keys_and_values[key] = value

print(keys_and_values)
