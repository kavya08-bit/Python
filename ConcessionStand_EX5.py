menu = {"Pizza":3.59,
        "Soda":1.50,
        "Hotdog":2.30,
        "fries":2.25}

cart=[]
total =0

print("------MENU------")
for key,value in menu.items():
    print(f"{key:10} : {value:.2f}")
print("-------------------")

while True:
    food=input("Select an item(q to quit)").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")
