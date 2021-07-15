''' 
This is a code to track what you ate and
what exercises you performed on daily basis.
This code is Written only to store all the information into
a text file.

'''


def getdate():
    import datetime
    return datetime.datetime.now()


# noinspection PyBroadException
try:
    def log():
        print("Do you want to Log Food or Exercise?")
        n = int(input("To Log Food Press 1\nTo Log Exercise Press 2\n"))
        name = input("Enter name of the client.\n")
        if n == 1:
            with open(name, "a") as op:
                food = input("Enter what you ate in a line!\n")
                op.write(f"Food\n{str([str(getdate())])}-->{food}\n")
                print('Successfully Written')
        elif n == 2:
            with open(name, "a") as op:
                exercise = input("Enter what exercise did you perform today in a line!\n")
                op.write(f"Exercise\n{str([str(getdate())])}-->{exercise}\n")
                print('Successfully Written')
        else:
            print("Invalid Entry!")


    def retrieve():
        name = input("Enter the name of the Client\n")
        with open(name, "r") as op:
            for i in op:
                print(i, end=" ")


    def health():
        print("You want to Log the data or Retrieve?\n")
        num = int(input("To Log Press 1\nTo Retrieve Press 2\n"))
        if num == 1:
            log()
        elif num == 2:
            retrieve()
        else:
            print("Invalid Entry!")


    print("Welcome to Health Tracking System!\n")
    health()
    while True:
        ans = input("Do you want to make changes again? y/n\n")
        if str.lower(ans) == 'y':
            health()
        else:
            print("Thank you for Coming!")
            break
except Exception as e:
    print('No such File Exists!')
