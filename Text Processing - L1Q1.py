data = input()

while not data == "end":
    reversed_data = data[::-1]
    print(f"{data} = {reversed_data}")
    data = input()