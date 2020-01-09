
#outlining the rules
print("This is Katarina's two player dice game")
print("There are 5 rounds, in one round, each player rolls two 6-sided dice. The total scores of these two rolls are then compared and then the winner of the round is decided.")
print("The Rules are as follows:")
print("-Each roll a player does is added onto their total score.")
print("-If the total number of the roll is even then an additional 10 points are added to their score.")
print("-If the total number of the roll is odd then 5 points are subtracted from their total score.")
print("-A players score cannot go below 0 at any point.")

#constants used for the log in, where the program compares the users log in details with these, allowing them to enter 
usernamecorrect = "username1234"
passwordcorrect = "password1234"

#player can either be X or Y (resembling player1 or player2). the programs starts it with player1 being X
player = "X"

#totalscores for each player that adds up throughout the whole game and is used to calculate the overall winner
totalscore1 = 0
totalscore2 = 0

#total score per round used to enter in the text file
roundend1 = 0
roundend2 = 0

#funtion for the login of the user. while loops used so that the game wont start until the correct details for both players are entered
def login():
    
    username = input(player1name + ", what is the username?")

    while username != usernamecorrect:
        print("Username incorrect")
        username = input(player1name + ", what is the username?")

    password = input(player1name + ", what is your password?")

    while password != passwordcorrect:
        print("Password incorrect. Try again.")
        password = input(player1name + ", what is your password?")
    
    print("log in successful")

    username = ""
    password = ""

    username = input(player2name + ", what is the username?")

    while username != usernamecorrect:
        print("Username incorrect")
        username = input(player2name + ", what is the username?")

    password = input(player2name + ", what is your password?")

    while password != passwordcorrect:
        print("Password incorrect. Try again.")
        password = input(player2name + ", what is your password?")
    
    print("log in successful")

#time module used to allow time.sleep (making the program slow down)
import time

#input statements for each players preferred name
player1name = str(input("Player 1, enter your name : "))
player2name = str(input("Player 2, enter your name : "))

#funciton call for log in
login()

##############

#clears the text file every time the games runs
with open("E:\Computing Course Work\Highscores.txt", "w") as writefile:
    writefile.write("")

##############

#for statement that loops 5 times, 1 for every round
for i in range(0,5):
    #for statement that loops 2 times, so every round it runs twice so 1 go for each player per round
    for x in range(0,1):
        
        #at the beginning of every players go, roll1 + roll2 + totalroll is set to 0 so the last go doesnt affect it
        roll1 = 0
        roll2 = 0
        totalroll = 0

        print(" ")
        #userinput to let them game know when they are ready to roll
        roll = input(str("Are you ready?"))

        if roll == "yes":
            
            import random
            roll1 = random.choice([1,2,3,4,5,6])
            roll2 = random.choice([1,2,3,4,5,6])
            totalroll = roll1 + roll2
            
            ##############
        
            if player == "X":

                print(" ")
                print(player1name + ", it is your turn...")

                time.sleep(1)

                print(" ")
                print("You rolled a " + str(roll1))
                print("You rolled a " + str(roll2))
                print(" ")
                
                roundend1 = totalroll
                totalscore1 = totalscore1 + totalroll

                if totalroll % 2 == 0:
                    totalscore1 = totalscore1 + 10
                    print("Your total is even. Extra 10 points awarded.")
                    roundend1 = roundend1 + 10
                else:
                    totalscore1 = totalscore1 - 5
                    print("Your total is odd. Minus 5 points.")
                    roundend1 = roundend1 - 5
                if roll1 == roll2:
                    roll3 = str(input("You got doubles. Do you want to roll again?"))
                    import random
                    roll3 = random.choice([1,2,3,4,5,6])
                    totalscore1 = totalscore1 + roll3
                    roundend1 = roundend1 + roll3

                if totalscore1 < 0:
                   print("Your score has dropped below 0. Therefore, your score has been reset to 0.")
                   totalscore1 = 0
                time.sleep(2)
                
                print(" ")
                print(player1name, ", your go is over. Your total score for this round is ", totalscore1)
                print(" ")
                
                player = "Y"

            ##############
                
            else:

                print(" ")
                print(player2name + ", it is your turn...")

                time.sleep(1)
                
                print(" ")
                print("You rolled a " + str(roll1))
                print("You rolled a " + str(roll2))
                print(" ")
                
                roundend2 = totalroll
                totalscore2 = totalscore2 = totalroll

                if totalroll % 2 == 0:
                    totalscore2 = totalscore2 + 10
                    print("Your total is even. Extra 10 points awarded.")
                    roundend2 = roundend2 + 10
                else:
                    totalscore2 = totalscore2 - 5
                    print("Your total is odd. Minus 5 points.")
                    roundend2 = roundend2 - 5

                if roll1 == roll2:
                    roll3 = str(input("You got doubles. Do you want to roll again?"))
                    if roll3 == "yes":
                        import random
                        roll3 = random.choice([1,2,3,4,5,6])
                        totalscore2 = totalscore2 + roll3
                        roundend2 = roundend2 + roll3

                if totalscore2 < 0:
                    print("Your score has dropped below 0. Therefore, your score has been reset to 0.")
                    totalscore2 = 0
                time.sleep(2)
                
                print(" ")
                print(player2name, ", your go is over. Your total score for the end of this round is ", totalscore2)
                print(" ")
                
                player = "X"

            ##############

            print("Round ", int(i + 1), " over")
            print(" ")

            ##############

        if totalscore1 > totalscore2:
            print(player1name, " is in the lead with ", totalscore1, " points.")
            with open("E:\Computing Course Work\Highscores.txt", "a") as myfile:
                myfile.write(player1name + ", " + str(roundend1) + "\n")
        else:
            print(player2name, " is in the lead with ", totalscore2, " points.")
            with open("E:\Computing Course Work\Highscores.txt", "a") as myfile:
                myfile.write(player2name + ", " + str(roundend2) + "\n")

##############

whowon = str(input("Do you want to see the overall winner?"))
if whowon == "yes":
    print(" ")
    print("---------------Calculating---------------")
    print(" ")
    time.sleep(2)
    if totalscore1 > totalscore2:
        print(player1name + " has won the game with " + str(totalscore1) + " points!")
    elif totalscore2 > totalscore1:
        print(player2name + " has won the game with " + str(totalscore2) + " points!")

    print(" ")

##############

seescore = str(input("Do you want to see the highscores of this game?"))
if seescore == "yes":
    print(" ")
    print("---------------Scores---------------")
    print(" ")
    time.sleep(2)
    with open("E:\Computing Course Work\Highscores.txt", "r") as readfile:
        for i in readfile:
            print(i)

##############

print("Game over. Thanks for playing.")

time.sleep(60)


    
    
    
