# Snake-Water-Gun-Game-Python-
I am Pasting The code Here for those who run their codes in online IDEs.
This a game exactly clone to Rock-Paper-Scissors Game.
The only Difference is the name of the game.
Hope you'll Enjoy it!
Here we Go!


import random as r
try:
    def game():
        print("\n\n")
        global h
        global c
        h=0; c=0
        print("Your Points= ",h,"\nComputer's Points= ",c)
        n=int(input("How many times do you want to play the Game?\n\n"))
        i=0
        while(True):
            i=i+1
            if i==n+1:
                print("\nYour Total Points are= ",h,"\ncomputer's Total Points are= ",c,"\n")
                if h>c:
                    print("You are Winner!")
                elif c>h:
                    print("computer is Winner!")
                else:
                    print("This round is a draw!")
                break
            option=['s','w','g']
            print("Options are",option)
            choice=input("Enter among the available options\n")
            machine= r.choice(option)
            print(machine)
            if choice=='s' and machine=='s':
                print("Draw!")
                print(f"Your points {h}\n Computer's points {c}")
            elif choice=='s' and machine=='w':
                    print("You've Won!")
                    h=h+1
                    print(f"Your points {h}\n Computer's points {c}")
            elif choice=='s' and machine=='g':
                    print("You've Lost!")
                    c=c+1
                    print(f"Your points {h}\n Computer's points {c}")
            elif choice=='w' and machine=='s':
                    print("You've Lost!")
                    c=c+1
                    print(f"Your points {h}\n Computer's points {c}")
            elif choice=='w' and machine=='w':
                    print("Draw")
                    print(f"Your points {h}\n Computer's points {c}")
            elif choice=='w' and machine=='g':
                    print("You've won!")
                    h=h+1
                    print(f"Your points {h}\n Computer's points {c}")
            elif choice=='g' and machine=='s':
                    print("You've Won!")
                    h=h+1
                    print(f"Your points {h}\n Computer's points {c}")
            elif choice=='g' and machine=='w':
                    print("You've Lost!")
                    c=c+1
                    print(f"Your points {h}\n Computer's points {c}")
            elif choice=='g' and machine=='g':
                    print("Draw!")
                    print(f"Your points {h}\n Computer's points {c}")
            else:
                print("Wrong Entry. Try again!")
            
                
                
    print("Welcome to Snake-Water-Gun Game.\n")
    print("Note: enter all the entries in small letters.")
    
    game()
   
    chance=input("Do you Want to Play again? y/n?\n")
    if chance=='y':
        game()
    else:
        print('Thank You for Playing!')
except Exception as e:
    print("Invalid Entry!")
