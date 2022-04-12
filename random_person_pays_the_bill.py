# Split string method
import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
name = len(names)
random_choice = random.randint(0, name-1)
payer = names[random_choice]
print(payer)
