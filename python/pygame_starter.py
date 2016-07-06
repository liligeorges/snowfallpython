"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
from random import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ROSY_BROWN = (255, 193, 193)



pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop ----------
x = 350  4m3
y = 250
speed = -5
original_speed = speed
#speed = randint(-10,11)
if speed == 0:
	speed = 1
print(speed)
y_move = speed
x_move = speed
radius = randint(20, 81)

while not done:
	
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
			
			#line(BLACK, (0,0), (700, 500), 1)
    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
		
    # If you want a background image, replace this clear with blit'ing the
    # background image.
	screen.fill(GREEN)

		

		
		#print(move)
		#move = False
		#input("Press enter")
    # --- Drawing code should go here
	pygame.draw.circle(screen, BLUE, (x , y), radius, 0)
	#x_move = 2
	x += x_move
	y += y_move

	if y >= 500:
		
		if original_speed < 0:
			y_move = speed
		else:
			y_move = -speed
	if x >= 700:
		if original_speed < 0:
			x_move = -(-speed)
		else:
			x_move = -speed
	if y <= 0:
		if original_speed < 0:
			y_move = -speed
		else:
			y_move = speed
	if x <= 0:
		if original_speed < 0:
			x_move = -speed
		else:
			x_move = speed
		
    # --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

    # --- Limit to 60 frames per second
	clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE