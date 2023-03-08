
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_items = len(names)

random_choice = random.randint(0, num_items -1) 

person_who_will_pay = names[random_choice]

print(person_who_will_pay + "It's going to buy the meal today")
