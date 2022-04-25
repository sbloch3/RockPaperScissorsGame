'''
Code a "Rock, Paper, Scissors" Game

@author: Sarah Bloch
'''
#Today I will be coding a "Rock, Paper, Scissors" game.
#The objective is to correctly code a "Rock, Paper, Scissors" game for an
#individual to play. This will be written by Sarah Bloch

#import random
import random 
from turtledemo.sorting_animate import Block

#Make a boolean variable called keepPlaying to track whether they want
#to keep playing and set it to True
keepPlaying = True

#LOOP 1: Make a game loop that continues while keepPlaying is True
# while (keepPlaying): "code block" when game stops: put to false
#loop needs tab

print("Welcome to Rock Paper Scissors!")
print("Best two out of three. Press 'q' to quit")
    
#make variables called userScore and cpuScore to track scores both set to 0
cpuScore = 0
userScore = 0    
    
#LOOP 2: Make a round loop while userScore or cpuScore is less than 2
while(userScore < 2 and cpuScore < 2 and keepPlaying):
    
#LOOP 3: Use input() to get a choice from the user 
#(rock, paper or scissors, or "q" {quit})
#store choice in variable. in this variable. Use .lower() to make the user's choice all lowercase
    
    Choice = input("Please choose (Rock, Paper, Scissors): ").lower()

        #Make a list of choices, then use random.choice() to get a random
        #choice for the cpu. Store the choice in a variable
    choiceList = ("rock", "paper", "scissors")
    cpuChoice = random.choice(choiceList)
    
    
    
    if ((Choice == "rock" and cpuChoice == "rock") 
        or (Choice == "paper" and cpuChoice == "paper") 
        or (Choice == "scissors" and cpuChoice == "scissors")):
            print("DRAW")
    #print("User: " + str(userScore) + " CPU: " + str(cpuScore))
   
   
    elif ((Choice =="rock" and cpuChoice == "paper") 
    or (Choice == "paper" and cpuChoice == "scissors")
    or (Choice == "scissors" and cpuChoice == "rock")):
            cpuScore = cpuScore + 1
    #print("User: " + str(userScore) + "CPU: " + str(cpuScore))
    
    elif ((Choice == "rock" and cpuChoice == "scissors") 
    or (Choice == "paper" and cpuChoice =="rock") 
    or (Choice == "scissors" and cpuChoice == "paper")):
        userScore = userScore + 1
    
    elif (Choice == "q"):
        keepPlaying = False
        
    else: print("Not an option, try again.")
    
    
    print("User: " + str(userScore) + " CPU: " + str(cpuScore))
    
      
print ("Thanks for playing!")

if Choice > cpuChoice:
    print ("CPU wins!")
else:
    print ("User wins!")

print("User: " + str(userScore) + " CPU: " + str(cpuScore))
keepPlaying = True

    #print("Not an option, try again") if(choice.lower() == "q"):
    #keepPlaying = False

#print("Thanks for playing!")

        #Make a if/elif.else statement to check users input against
        #cpu's choice
        #NOTE: you will have to compare the users choice and cpu's choice to 
        #"rock", "paper" and "scissors" seperately and combine with logical operators

                #print ("DRAW")
                #print ("User: " + str(userScore) + "CPU: " + str(cpuScore))

                #also adjust to different outcomes not just ties
        #if the user won, add one to the users score, then print out the scores
            #"User: [#]. CPU:[#]"
            
        #elif if (elif) the computer won, add one to the computer score
        #print out the scores...
        
        #else if it is a draw, print "DRAW", then print out the scores...
        
        #else if the user entered "q", then end the round and the game loop
        #use a break statement to end a round (round loop). Make keepPlaying equal False
        
        #else the user didn't enter accepted input, print"not an option, try again"    
        #if(choice.lower() == "q"):
            #keepPlaying = False
    #print out thank you message
    #print who won
        #if the userScore is 2, then the user won
            #code
        #elif the cpuScore is 2, than the CPU won
            #code
    #print out the final scores (same code above)
        
        
        
          






