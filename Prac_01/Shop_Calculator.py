number_of_items = int(input("Number of Items: "))
while number_of_items < 1:
    print("Invalid Number of Items!")
    number_of_items = int(input("Number of Items: "))
current_price = 0
for loop in range(number_of_items, 0, -1):
    price = float(input("Price of Item: $"))
    current_price = current_price + price
print("$ {:.2f}".format(current_price))
