import random as rn

# noinspection PyBroadException
try:
    def rock():
        i = 0
        n = int(input("How many times do you want to play the game?\n"))
        option = ['s', 'w', 'g']
        h = 0
        c = 0
        print(f"Your Points are {h}\nComputer's Points are {c}\n")
        while True:
            i = i + 1
            if i == n + 1:
                print("You've exhausted your trials!")
                print(f"Your Total Points are {h}\n and Computer's Total Points are {c}\n")
                if h > c:
                    print("You are the Winner!")
                elif h < c:
                    print("Computer is Winner!")
                else:
                    print("It's a Tie!")
                break
            print("Options are\ns  = snake\nw  = water\ng  = gun")
            choose = input("Enter among the options given\n")
            machine = rn.choice(option)
            print(machine)
            if choose == machine:
                print("Tie!")
                print(f"Your Points are {h}\nComputer's Points are {c}\n")
            elif choose == 's' and machine == 'w':
                print("You win!")
                h = h + 1
                print(f"Your Points are {h}\nComputer's Points are {c}\n")
            elif choose == 's' and machine == 'g':
                print('You lost!')
                c = c + 1
                print(f"Your Points are {h}\nComputer's Points are {c}\n")
            elif choose == 'w' and machine == 's':
                print("You lost!")
                c = c + 1
                print(f"Your Points are {h}\nComputer's Points are {c}\n")
            elif choose == 'W' and machine == 'g':
                print('You win!')
                h = h + 1
                print(f"Your Points are {h}\nComputer's Points are {c}\n")
            elif choose == 'g' and machine == 'w':
                print("You lost!")
                c = c + 1
                print(f"Your Points are {h}\nComputer's Points are {c}\n")
            elif choose == 'g' and machine == 's':
                print('You win')
                h = h + 1
                print(f"Your Points are {h}\nComputer's Points are {c}\n")
            else:
                print("Invalid Entry!")
    print("Welcome to Snake-Water-Gun game!\n\n")
    print("Warning!\nPlease Enter all the entries in small letters.\n")
    rock()
    ans = input("Do you Want to play the game again? y/n\n")
    if ans == 'y':
        rock()
    else:
        print("Thank you for playing!")
except Exception as e:
    print("Invalid Entry!")
