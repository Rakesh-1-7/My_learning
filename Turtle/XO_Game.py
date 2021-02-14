import turtle
from itertools import permutations

My_turtle = turtle.Turtle()
My_turtle.ht()
turtle.Screen().bgcolor("OrangeRed") 

positions = [(-65,125), (35,125), (135,125), (-65,25), (35,25),(135,25),(-65,-75),(35,-75), (135,-75)]

def O_printer(x):
  My_turtle.penup()
  My_turtle.goto(positions[x])
  My_turtle.pendown()
  My_turtle.color("white")
  My_turtle.write("O",font=("Calibri",40,"bold" ))

def X_printer(x):
  My_turtle.penup()
  My_turtle.goto(positions[x])
  My_turtle.pendown()
  My_turtle.color("white")
  My_turtle.write("X",font=("Calibri",40,"bold"))

def square(x=100):
  My_turtle.speed(0)
  for i in range(4):
    My_turtle.fd(x)
    My_turtle.lt(90)

def winner_declare(x="",y=""):
    My_turtle.penup()
    My_turtle.goto(-250,0)
    My_turtle.write("Game over...! " + x +", "+ y +" wins.", font=("Arial",30,"bold"))


for i in range(4):
  square()
  My_turtle.rt(90)

My_turtle.fd(100)
for i in range(2):
  square()
  My_turtle.rt(90)

My_turtle.rt(90)
My_turtle.fd(100)
square()
My_turtle.rt(90)
square()
My_turtle.lt(180)
My_turtle.fd(100)
My_turtle.rt(90)
square()
turn = 0
list_of_used_positions = []
list_of_O_positions = []
list_of_X_positions = []
Game_over = False

win_comb = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

while turn <= 8 and Game_over != True :
    if turn == 0:
        Player_1 = input("Enter the name of player 1 : ")
        Player_2 = input("Enter the name of player 2 : ")


    x = int(input("\nEnter a number from 1 to 9 : "))
    if x < 1 or x > 9:
        print("\nInvalid Position...! Try again!")
        continue

    if x in list_of_used_positions:
        print("The position is already occupied.")
        continue

    list_of_used_positions.append(x)
    if turn%2 == 0:
        X_printer(x-1)
        list_of_X_positions.append(x-1)
        
    else:
        O_printer(x-1)
        list_of_O_positions.append(x-1)
    turn += 1


    if turn > 4 and turn <= 7:
        for o in list(permutations(list_of_O_positions,3)):
            for i in range(len(win_comb)):
                a = win_comb[i]
                if (o == a):
                    Game_over = True
                    My_turtle.clear()
                    winner_declare("O",Player_2)
        for o in list(permutations(list_of_X_positions,3)):
            for i in range(len(win_comb)):
                a = win_comb[i]
                if (o == a):
                    Game_over = True
                    My_turtle.clear()
                    winner_declare("X",Player_1)
                    
if turn == 9:
    My_turtle.clear()
    My_turtle.penup()
    My_turtle.goto(-250,0)
    My_turtle.pendown()
    My_turtle.write("Game over... It's a draw...!",font=("Arial",30,"bold"))


input()
My_turtle.clear()




