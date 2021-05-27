# Snake Water gun
import random as ran
import time

choice_list = [1, 2, 3]
# 1 = Snake
# 2 = Water
# 3 = Gun


print("Welcome to the game\nSnake Water and Gun\n")
name = input("Enter your name")
print("Hello " + name + " welcome to the game\n\n")
print("..........")
print("Instructions:\nIf 1 is snake and 2 is water -1 is winner\n"
      "If 1 is water and 2 is gun   -1 is winner\n"
      "If 1 is snake and 2 is gun   -2 is winner\n")
print("..........")
time.sleep(1)
# win is a variable to store the number of matches won
# i is a normal variable
win = 0
i = 0

while i < 10:
	print("You have " + str(10 - i) + " chances left")
	i = i + 1
	choice = int(ran.choice(choice_list))
	# choice- it is the choice of the computer

	user = int(input("Enter your choice\n1.Snake\n2.Water\n3.Gun"))  # ask users feed
	print("Yor choice is " + str(user) + "\n")

	while choice == 1:  # snake
		if user == 1:  # snake
			print("The match is a draw\n")
			print("..........")
			time.sleep(1)
			break

		elif user == 2:  # water
			print("You loose,Computer wins\n")
			print("..........")
			time.sleep(1)
			break

		elif user == 3:  # gun
			print("You win\n Congratulations\n")
			print("..........")
			time.sleep(1)
			win = win + 1
			break

		else:
			print("Invalid choice\n")
			print("..........")
			time.sleep(1)
			break

	while choice == 2:  # water
		if user == 1:  # snake
			print("You win\nCongratulations\n")
			print("..........")
			time.sleep(1)
			win = win + 1
			break

		elif user == 2:  # water
			print("The match is a draw\n")
			print("..........")
			time.sleep(1)
			break

		elif user == 3:  # gun
			print("You loose,Computer wins\n")
			print("..........")
			time.sleep(1)
			break

		else:
			print("Invalid choice\n")
			print("..........")
			time.sleep(1)
			break

	while choice == 3:  # gun
		if user == 1:  # snake
			print("You loose,Computer wins\n")
			print("..........")
			time.sleep(1)
			break
		elif user == 2:  # water
			print("You win\nCongratulations\n")
			print("..........")
			time.sleep(1)
			win = win + 1
			break
		elif user == 3:  # gun
			print("The match is a draw\n")
			print("..........")
			time.sleep(1)
			break
		else:
			print("Invalid choice\n")
			print("..........")
			time.sleep(1)
			break

# print(win)
lost = 10 - win
points = str(win)
if win >= 5:
	print("Congratulations You have won the match")
	print("Your total points are " + points)
	time.sleep(1)




else:
	print("You loose")
	print("Your total points are " + points)
print("..........")
time.sleep(1)
print("The end")
