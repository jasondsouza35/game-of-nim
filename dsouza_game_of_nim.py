#Author: Jason D'Souza
#Date: November 5, 2019
#File Name: dsouza_game_of_nim.py
#Description: Program functions as a game starting with a total of 15 to 30 stones, computer and user alternate taking 1 to 3 stones, the last one to take the remaining stones loses

import random #Imports random variable to be used for randomized computer turns

def autoturn(): #Defines 'autoturn' function to be used to determine what the computer plays
    global total #Global function allows the use of the total 'variable' and 'c' variable from outside the function
    global c
    if total >= 3: #If statement continues if the total amount of stones is greater than 3
        auto = random.randint(1,3) #'Auto' variable assigns a random turn value for the computer, taking 1 to 3 stones
        total = total - auto #'Auto' value is subtracted from the total variable
        print('Computer turn:', auto) #Prints the amount of stones taken (the 'auto' value)
        c += 1 #'c' variable counts which turn the computer is on and adds one
        print('Stones remaining:', total) #Prints 'total' variable, which is the remaining stones
    elif total <= 2: #If statement continues if the total amount of stones is less than or equal to 2
        auto = random.randint(1,total) #Random turn for computer, allows the value for the auto variable to either be 1 or 2 but prevents it from being greater than the 'total' value
        total = total - auto
        print('Computer turn:', auto) 
        c += 1
        print('Stones remaining:', total)

def playercheck(): #Defines 'playercheck' function to check if the player is assign 'valid' values
    global total #Global function is used to allow the use of the 'total' and 'player' variables from outside the function
    global player
    while player > total or player > 3 or player < 1: #While statement continues if the user input for the 'player' variable is greater than 3 or the 'total', or less than 1
        print('') #Prints a space for organization
        print('Turn invalid')
        player = int(input('How many stones would you like to take:')) #Accepts another input from the user for the 'player' variable


action = '' #Defines the 'action' variable

while action != 'S':
    action = str(input('Print S to start, H for help, or Q to quit:')) #Menu, accepts user input as a string
    action = action.upper() #Function converts the input for 'action' to uppercase in case the user types a lowercase input
    print('') 
    
    if action == 'H': #If user types 'H' for the 'action' variable, prints what the program does and how to use it
        print('This is the Game of Nim!')
        print('You will start with a random number of stones in a stack from a range of range 15 to 30.') #User instructions
        print('You and a bot will compete taking 1 to 3 stones from the stack each turn. You cannot take more stones then there are in the stack.')
        print('The last player to take the stones loses.')
        print('')

    if action == 'Q': #Quits if the user types 'Q' for the 'action' variable
        quit()

    if action == 'S':#Starts the game if the user types 'S' for the 'action' variable
        total = random.randint(15,30) #Defines the 'total' variable and determines a random value from 15 to 30 to be the total "stones" for the game
        print('This match will have', total, 'stones')
        print('')
        c = 0 #Defines a counter variable for the computer
        c1 = 0 #Defines a counter variable for the user

        while total > 0: #While loop continues the game until there are no stones left
            autoturn() #Computer turn function plays
            if total == 0: #If there are no more stones remaining after the computer turn so when 'total' equals 0, the while loop breaks
                break
            player = int(input('How many stones would you like to take:')) #User's turn, accepts amount of stones for the 'player' variable as a integer
            playercheck() #Function checks if the 'player' value from the user meets the conditions for the game
            total = total - player 
            c1 += 1 #Counter counts the turn for the user
            print('Stones remaining:', total) #Prints amount of stones remaining
            if total == 0: #If there are no more stones remaining after the user turn, the while loop breaks
                break
            print('')

print('')
print('There are no more stones remaining') #Prints there are no more stones remaining after the previous while loop has broken, hence the game has ended    
if c > c1: #If statement continues if the counter variable for the computer is greater than the counter variable for the user, if the computer has a greater counter value, that means it took the last move and lost
    print('Player has won') #Prints that the player won
elif c == c1: #If the counter values are the same, the user took the last move and lost
    print('Computer has won')




