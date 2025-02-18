import random

def jeu_devine_nombre():
    nombre_secret = random.randint(1,100)
    tentatives = 0
    max_tentatives = 10

    print("welcome to the game")
    print("Try to find the number between 1 and 100")


    while tentatives < max_tentatives:
        try:
            tentative = int(input(f"Try {tentatives + 1}/{max_tentatives} : "))
        except ValueError:
            print("Put a real number")
            continue

        tentatives += 1

        if tentative < nombre_secret :
            print("Try a bigger number")
        elif tentative > nombre_secret :
            print("Try a little number")
        else :
            print("good job ! you win the game, you find the number in {tentatives}")
            break

    else :
        print("You loose")

    rejouer = input("Do you want to retry ? (y/n)")
    if rejouer.lower() == 'y':
        jeu_devine_nombre()

jeu_devine_nombre()




