import random
print("Coinflip Generator")
yes = input("would you like to flip the coin? y/n\n")
if yes == "y":
  random_side = random.randint(1, 2)
  if random_side == 1:
    print("heads")
  if random_side == 2:
    print("tails")
if yes == "n":
  print("get off then")
