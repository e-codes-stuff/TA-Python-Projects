# eliminate the "\n" at the start of every print string
def nprint(string):
    print("\n{}".format(string))

def start(nice=0, mean=0, name=""):
    name = describe_game(name)
    nice, mean, name = nice_mean(nice,mean,name)

def describe_game(name):
    if name != "":
        nprint("Thank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    nprint("Welcome, {}!".format(name))
                    nprint("In this game, you will be greeted \nby several different people.\nYou can choose to be nice or mean")
                    nprint("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name
    
def nice_mean(nice, mean, name):
    stop = True
    while stop:
        show_score(nice, mean, name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>> ").lower()
        if pick == "n":
            nprint("The stranger walks away smiling...")
            nice += 1
            stop = False
        elif pick == "m":
            nprint("The stranger glares at you \nmenacingly and storms off...")
            mean += 1
            stop = False
    score(nice, mean, name)

def show_score(nice, mean, name):
    nprint("{}, your current total: \n{} Nice, and {} Mean".format(name, nice, mean))

def score(nice, mean, name):
    if nice > 2:
        win(nice, mean, name)
    elif mean > 2:
        lose(nice, mean, name)
    else:
        nice_mean(nice, mean, name)

def win(nice, mean, name):
    nprint("Nice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    again(nice, mean, name)

def lose(nice, mean, name):
    nprint("Ahhh too bad, game over!\n{}, you were too mean!")
    again(nice, mean, name)

def again(nice, mean, name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        elif choice == "n":
            nprint("Oh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            nprint("Enter Y for 'YES' and N for 'NO':\n>>> ")

def reset(nice, mean, name):
    nice = 0
    mean = 0
    start(nice, mean, name)

if __name__ == "__main__":
    start()