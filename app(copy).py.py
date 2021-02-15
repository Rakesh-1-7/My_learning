import pandas as pd
import numpy as np
import random

# Enter the file path with extension
file_name = input("Enter the file name : ")

file1 = open(file_name,"r")
x = file1.readlines()

# Removing white spaces and new line characters in the array elements.
for i in range(len(x)):
    x[i] = x[i].strip("[\n ]")

numbers = x[0].split(' ')
total_pizzas = int(numbers[0])
teams_with_2_member = int(numbers[1])
teams_with_3_member = int(numbers[2])
teams_with_4_member = int(numbers[3])
pizza_delivered = []
# Getting the info of only the pizzas
pizzas = x[1:]
x = 0
while x < total_pizzas:
  pizzas[x] = str(x)+" "+ pizzas[x]
  x+=1

pizzas.sort(key = lambda y:(y.split())[1],reverse=True)

# Creating a copy of the pizzas so that the original list is preserved.
pizza_copy = pizzas
# print(total_pizzas)
pizza_data = []

# Splitting the pizzas into number of ingedients and the ingredients
x = 0
while x < len(pizza_copy):
    pizza_data.append(np.array(pizza_copy[x].split(' ',2) ))
    x += 1

df = pd.DataFrame(data = pizza_data)
df = df.rename(columns={0:'Pizza_number',1:'Number_of_ingredients',2:'Ingredients'})
df.head(50)

# print(df.head())

def pizza_to_2_member_teams():

    random_index_1 = random.randint(0,total_pizzas-1)
    random_pizza_1 = df.Ingredients[random_index_1].split()

#   To remove the common ingredients, and get the unique ones.
    counter = 0
    while(counter < total_pizzas) :
        c = score(random_pizza_1 + df.Ingredients[counter].split() )
        if c > 7:
            pizza_delivered.append(2)
            pizza_delivered.append(random_index_1)
            pizza_delivered.append(counter)
            print(c**2)
            df.pop(random_index_1)
            df.pop(counter)
            break 
        else:
            counter += 1 

def score(x):
    return len(x)

pizza_to_2_member_teams()
print(pizza_delivered)











