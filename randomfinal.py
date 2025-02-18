import random

def langue():
    langue = input("What is your language? Quel est votre langue? (english/francais) : ").lower()
    if langue == 'francais':
        jeu_devine_nombre()
    else:
        play_number()

def jeu_devine_nombre():
    nombre_secret = random.randint(1, 100)
    tentatives = 0
    max_essais = 10

    print("🎯 Bienvenue dans le jeu de devinette !")
    print("Essayez de deviner le nombre entre 1 et 100.")

    while tentatives < max_essais:
        try:
            tentative = int(input(f"🔢 Tentative {tentatives + 1}/{max_essais} : "))
        except ValueError:
            print("❌ Entrez un nombre valide.")
            continue

        tentatives += 1

        if tentative < nombre_secret:
            print("🔼 Trop bas ! Essayez encore.")
        elif tentative > nombre_secret:
            print("🔽 Trop haut ! Essayez encore.")
        else:
            print(f"🎉 Bravo ! Vous avez trouvé en {tentatives} tentatives.")
            break
    else:
        print(f"😞 Vous avez épuisé vos {max_essais} essais. Le nombre était {nombre_secret}.")

    rejouer = input("Voulez-vous rejouer ? (o/n) : ")
    if rejouer.lower() == 'o':
        jeu_devine_nombre()

def play_number():
    nombre_secret = random.randint(1, 100)
    tentatives = 0
    max_tentatives = 10

    print("Welcome to the game!")
    print("Try to find the number between 1 and 100.")

    while tentatives < max_tentatives:
        try:
            tentative = int(input(f"Try {tentatives + 1}/{max_tentatives} : "))
        except ValueError:
            print("Put a real number.")
            continue

        tentatives += 1

        if tentative < nombre_secret:
            print("Try a bigger number.")
        elif tentative > nombre_secret:
            print("Try a smaller number.")
        else:
            print(f"Good job! You win the game, you found the number in {tentatives} attempts.")
            break
    else:
        print(f"You lose! The number was {nombre_secret}.")

    rejouer = input("Do you want to retry? (y/n) : ")
    if rejouer.lower() == 'y':
        play_number()

# Lancer le programme en demandant la langue
langue()






