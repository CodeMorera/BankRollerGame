import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

list=len(names)-1
payer = names[random.randint(0,list)]
print(f"{payer} is going to buy the meal today!")