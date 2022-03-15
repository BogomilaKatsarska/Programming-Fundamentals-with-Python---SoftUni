products = input().split()
stock_dict = {}

for el in range(0, len(products), 2):
    key = products[el]
    value = int(products[el+1])
    stock_dict[key] = value


searched_products = input().split()

for el in range(len(searched_products)):
    if searched_products[el] in stock_dict:
        print(f"We have {stock_dict[searched_products[el]]} of {searched_products[el]} left")
    else:
        print(f"Sorry, we don't have {searched_products[el]}")