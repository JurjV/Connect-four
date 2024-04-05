from repo import Repo
from screen import Screen
from service import Service
from ui import Console

# Connect four

while True:
    print("What kind of interface would you like the game to have?")
    print("1.Console driven interface")
    print("2.Graphical interface")
    print("x.None,exit")
    opt = input(">")
    if opt not in ["1", "2", "x"]:
        print(f"\"{opt}\" is not a valid option!")
    else:
        if opt == "x":
            break
        elif opt == "2":
            repo = Repo()
            service = Service(repo)
            screen = Screen(service)
            console = Console(service, screen)
            console.run_console_graphical()
        else:
            repo = Repo()
            service = Service(repo)
            console = Console(service, None)
            console.run_console()
