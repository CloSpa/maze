# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
import pickle
from classes import Carte, Robot

def choose_map():

    # ON CHARGE LES CARTES EXISTANTES
    cartes = []

    for nom_fichier in os.listdir("cartes"):

        if nom_fichier.endswith(".txt"):
            chemin = os.path.join("cartes", nom_fichier)
            nom_carte = nom_fichier[:-4].lower()

            with open(chemin, "r") as fichier:
                lignes = fichier.read().split("\n")
            cartes.append((nom_carte, lignes), )

    # ON AFFICHE LES CARTES EXISTANTES
    print("\nBienvenue dans Roboc !")
    print("\nChoisissez votre labyrinthe :")

    for i, carte in enumerate(cartes):
        print("  {} - {}".format(i + 1, carte[0]))

    # ON DEMANDE A L'UTILISATEUR DE CHOISIR SA CARTE
    num_carte_choisie = input("\nEntrez le numéro de votre choix pour commencer à jouer :\n> ")

    while num_carte_choisie.isdigit() is False or int(num_carte_choisie) not in range(1, len(cartes) + 1):
        num_carte_choisie = input("Veuillez renseigner le numéro de la carte choisie\n> ")

    # ON CREE LA CARTE SELON LE CHOIX DE L'UTILISATEUR
    nom_carte = cartes[int(num_carte_choisie) - 1][0]

    carte_choisie = Carte(nom_carte, cartes[int(num_carte_choisie) - 1][1])
    carte_en_cours = Carte(nom_carte, cartes[int(num_carte_choisie) - 1][1])


# ON AFFICHE LES REGLES
rules = ("""


* * * * * Bienvenue dans le jeu, les règles sont les suivantes * * * * *


* * * SE REPERER * * *
=> Les murs sont formés de la lettre 'O', vous ne pouvez pas les franchir.
=> Les portes sont symbolisées par des '.', vous pouvez les traverser.
=> Votre robot est représenté par le "X".
=> La sortie du labyrinthe est en forme de "U".


* * * JOUER * * *
=> 'N', 'O', 'E' et 'S' vous permettent de vous diriger respectivement au Nord, à l'Ouest, à l'Est et au Sud.
=> Pour vous déplacer de plusieurs cases en un coup, il faut préciser le nombre de cases après la direction.
Par exemple, 'E3' vous déplace de 3 cases vers l'Est.
=> 'Q' vous permet de quitter la partie en sauvegardant.""")


#
# robot = Robot(carte_en_cours)
#
# # ON LANCE LA BOUCLE DE JEU
# should_keep_going = True
#
# while should_keep_going is True:
#     print("\n")
#     print(carte_en_cours)
#     action = input("\nNous vous écoutons\n> ").upper()
#
#     while action[0].isalpha() is False:
#         action = input("\nVous devriez essayer une lettre\n> ").upper()
#
#     while action[0] not in "QNOES":
#         action = input("\nNous ne connaissons pas cette lettre, veuillez réessayer\n> ").upper()
#
#     if len(action) > 1:
#         while action[1:].isdigit() is False:
#             action = input("\nLa drogue c'est mal, après une lettre, on met plutôt un chiffre\n> ").upper()
#         while action[1:] == 0:
#             action = input("\nMais enfin vous avez bu ? Relisez les règles !\n> ").upper()
#
#     # ON VERIFIE SI LE DEPLACEMENT EST POSSIBLE
#     if action[0] == "N":
#         robot.moveNord(action, carte_choisie, carte_en_cours)
#
#     elif action[0] == "O":
#         robot.moveOuest(action, carte_choisie, carte_en_cours)
#
#     elif action[0] == "E":
#         robot.moveEst(action, carte_choisie, carte_en_cours, should_keep_going)
#
#     elif action[0] == "S":
#         robot.moveSud(action, carte_choisie, carte_en_cours)
#
#     chemin = os.path.join("cartes", nom_carte + "_en_cours")
#     data_to_save = [nom_carte, robot.x, robot.y]
#
#     if action == "Q":
#         print("\nA bientôt !")
#         data_to_pickle = open(chemin, "wb")
#         pickle.dump(data_to_save, data_to_pickle)
#         data_to_pickle.close()
#         should_keep_going = False
#
#     # ON SAUVEGARDE LA PARTIE A CHAQUE COUP
#     data_to_pickle = open(chemin, "wb")
#     pickle.dump(data_to_save, data_to_pickle)
#     data_to_pickle.close()
#
#     if carte_choisie.lignes[robot.y][robot.x] == "U":
#         print(carte_en_cours)
#         os.remove(chemin)
#         should_keep_going = False
