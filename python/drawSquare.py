'''FIRST: make a for loop to repeat drawing the four sides of the square
make the dimensions 20 x 20
pen down and pen up

loop: 20 steps forward, turn left 90 degrees X  FOUR

bonus: user input to change the color, user input to change the size of the square
'''


from turtle import *

size = input("How big do you want the square to be?")
sizeUser = int(size)
fast = input("How fast do you want the square to be drawn?")
speedUser = int(fast)
userColor = input("What color do you want the square to be?")


goto(-100, 0)
for s in range(4):
	pendown()
	pencolor(userColor)
	speed(speedUser)
	forward(sizeUser)
	left(90)



