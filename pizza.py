print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
if size == "s":
  pizza = 15
if size == "m":
  pizza = 20
if size == "l":
  pizza = 25
if add_pepperoni == "y":
  if pizza == 15:
    pizza = pizza + 2
  if pizza == 20 or 25:
    pizza = pizza + 3
if extra_cheese == "y":
 pizza = pizza + 1

print(f"your total bill is ${pizza}")
