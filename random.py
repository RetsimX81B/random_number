import random

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

jeu_devine_nombre()
reak