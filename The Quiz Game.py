# My Quiz game

print("Welcome to the virtual Quiz Game")


playing = input("Would you like to play this game? ")


if playing == "yes":
    print("okay then let's start the game")

else:
    print("We are sorry to see you going;)")

answer = input("What is tha CPU stands for? ")

if answer == "central processing unit":
    print("Correct answer")
else:
    print("Incorrect answer")

answer = input("What is tha GPU stands for? ")

if answer == "graphic processing unit":
    print("Correct answer")
else:
    print("Incorrect answer")

answer = input("What is tha RAM stands for? ")

if answer == "random access memory":
    print("Correct answer")
else:
    print("Incorrect answer")

print("Congratulations you won the game:) ")