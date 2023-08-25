import random
from turtle import Turtle, Screen
my_screen = Screen()
my_screen.setup(width=800, height=400)
is_game = False
all_colors = ["red","green","azure4","maroon","yellow","orange"]
user_color = my_screen.textinput("Make a bet!","Who will win the race?Type the color")
print(user_color)
y_position = [-110,-70,-30,10,50,90]
all_turtle = []
for i in range(6):
    my_turtle = Turtle()
    my_turtle.shape("turtle")
    my_turtle.color(all_colors[i])
    my_turtle.penup()
    my_turtle.goto(-380, y_position[i])
    all_turtle.append(my_turtle)

if user_color in all_colors:
    is_game = True
else:
    print("Given color is not in the list! Check once")



while is_game:
    for turtles in all_turtle:
        if turtles.xcor() > 380:
            is_game = False
            if turtles.pencolor() == user_color:
                print(f"You've won! The winning color is {turtles.pencolor()}")
            else:
                print(f"You've lost!The winning color is {turtles.pencolor()}")
        rand_dist = random.randint(1,10)
        turtles.forward(rand_dist)


my_screen.exitonclick()

