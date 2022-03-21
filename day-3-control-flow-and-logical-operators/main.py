print("Welcome to Tresure Island.")
print("Your mission is to find the threasure.")
question = input("You're at a crossroad, where do you want to go? Type \"left\" or \"right\". ")

if question.lower() == "left":
    question = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to eait for a boat. Type \"swim\" to swim across. ")
    if question.lower() == "wait":S
        question = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose? ")
        if question.lower() == "yellow":
            print("You found the treasure! You Win!")A
        elif question.lower() == "red":
            print("It's a room full of fire. Game Over.")
        else:
            print("You enter a room of beasts. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
