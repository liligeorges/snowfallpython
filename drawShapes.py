import turtle
wn = turtle.Screen()
wn.colormode(255)
bob = turtle.Turtle()
bob.shape("turtle")
bob.speed(1)

def shape(sides, shapes, length, a, b, c):
	bob.penup()
	bob.goto(-400,50)
	for i in range(shapes):
		bob.penup()
		if sides >= 5:
			bob.forward(length + 30)
		else:
			bob.forward(length + 10)
		bob.pendown()
		if a >= 150:
			a -= 30.0
		else:
			a = 50
		if b <= 235:
			b += 70.0
		else:
			b = 255
		if c >= 150:
			c -= 30.0
		else:
			b = 255
		for i in range(sides):
			bob.pencolor(a, b, c)
			bob.forward(length)
			bob.right(360/sides)

def custom_shape(sides, length, a, b, c):
	bob.pencolor(a, b, c)
	bob.penup()
	bob.goto(-200, 50)
	bob.pendown()
	for i in range(sides):
		bob.forward(length)
		bob.right(360/sides)
	
choice = False
while choice == False:
	user_choice = int(input("(1)Premade Shape, (2)Custom Shape"))
	if user_choice == 1:
		sides = int(input("How many sides? "))
		shapes = int(input("How many shapes?"))
		if shapes == 1:
			length = 150
		elif shapes == 2:
			length = 100
		elif shapes == 3:
			length = 90
		elif shapes == 4:
			length = 80
		elif shapes >= 5:
			length = 50
		a = 255.0
		b = 20.0
		c = 255.0
		#bob.pencolor(a,b,c)
		shape(sides, shapes, length, a, b, c)
		choice = True
	
	elif user_choice == 2:
		distance = int(input("What do you want the length of the shape to be: "))
		red_value = int(input("What do you want your red value to be (0-255): "))
		green_value = int(input("What do you want your green value to be (0-255): "))
		blue_value = int(input("What do you want your blue value to be (0-255): "))
		sides = int(input("How many sides?"))
		custom_shape(sides, distance, red_value, green_value, blue_value)
		choice = True
	else:
		print("You must enter a choice.")