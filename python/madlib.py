name = input("What is your name?")
hobby = input("What is your favorite hobby?")
favoritePlace = input("Where is your favorite place to visit?")
favoriteAnimal = input("What is your favorite animal?")
petName = input("What would you name your pet?")
feel = input("How will you feel when you get your pet?")
moreAnimal = True

if favoriteAnimal == "Dog":
	print ("Wow, that is my favorite animal, too!")
else:
	print ("Wow, " + favoriteAnimal + "'s are cool!")
	
if favoritePlace  == "The beach":
	print ("I love the beach, too!")
else:
	print ("Wow, that place seems amazing!")

if feel == "Happy":
	print ("Yay, I'm happy for you!")
elif feel == "Sad":
	print ("Why?!?! You got a new " + favoriteAnimal + "??!?!?!?") 
elif feel == "Angry":
	print ("Did the " + favoriteAnimal + "cost too much? I'm sorry.")
else:
	print ("You should be happy you got a new pet!")



print ("One day, " + name + " was walking along, by herself, in search of her favorite animal, a " + favoriteAnimal)
print ("She was visiting " + favoritePlace + " and was very excited to meet new friends and family.")
print (name + " soon found a pet store! " + name + " walked inside, looking for a " + favoriteAnimal + ". She soon found the owner, who told her they had her " + favoriteAnimal + "!")
print (name + " was so " + feel + "!")
while moreAnimal == True:
	another = int(input("Do you want another " + favoriteAnimal + "? Yes: 1 No: 2"))
	howManyAnimal= int(input("Number: "))
	if another == 1:
		howManyAnimal += 1
	else:
		moreAnimal == False
print ("She wanted to spend a few hours on her favorite pastime, which was " + hobby)
print (name + " spent some time on doing her favorite hobby. Then the sun went down, and she had to go home to her new pet, " + petName + "!")