import random

names = input("Enter your friends names")
names_list = names.split(',')
print(names_list)
length = len(names_list)
random_choice= random.randint(0, length-1)
print(f'{names_list[random_choice]} is going to buy the meal today!')