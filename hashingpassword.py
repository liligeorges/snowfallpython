from hashlib import *


userLogin = {}

while True == True:

	choice = input("Do you want to login or sign up? 1) Login 2) Sign Up ")

	if choice == "1":
		name = input("Enter username: ")
		password = input("Enter password: ")
		if name not in userLogin or password not in userLogin:
			print("Invalid username/password.")
			newUser = input("Choose a username: ")
			newPass = input("Choose a password: ")
			newPass = sha256("newPass".encode('utf-8')).hexdigest() 
			login = {newUser: newPass}
			userLogin.update(login)
		else:
			print ("Congratulations! You're in!")
	else:
		newUser = input("Choose a username: ")
		newPass = input("Choose a password: ")
		login = {newUser: newPass}
		userLogin.update(login)