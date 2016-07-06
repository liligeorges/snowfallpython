''' Random Number Game!
Player tries to guess random number between 1-80
Player gets certain number of lives before game ends.
Has to be a whole number
Lives decrease by 1 every time guess is wrong
Once lives becomes 0 game over!
'''
 
import random 

print ("Welcome to the Random Number Game! You have three tries to guess a number between 1 and 80.")


randomNumber = random.randint(1,80)
livesRemaining = 3

answer = False

while answer == False:
	while livesRemaining  >0:
		livesRemaining -= 1
		userGuess = input("Guess a number: ")
		guessNumber = int(userGuess)
	
		if userGuess == randomNumber:
			print ("You won! Congrats!")
			answer=True
		if not guessNumber > 0 or not guessNumber < 81:
			print("That number is not between 1 and 80!")
		
		elif guessNumber > randomNumber:
			if livesRemaining>0:
				print ("The number is too big. Try again!")
	
		elif guessNumber < randomNumber:
			if livesRemaining>0: 
				print ("The number is too small. Try again!")
	
