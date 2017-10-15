# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
from classes import Carte, Robot


# On charge les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
    if nom_fichier.endswith(".txt"):
        chemin = os.path.join("cartes", nom_fichier)
        nom_carte = nom_fichier[:-4].lower()        

        with open(chemin, "r") as fichier:
            lignes = fichier.read().split("\n")
        cartes.append((nom_carte, lignes),)

# Si il y a une partie sauvegardée, on l'affiche, à compléter
#sauvegarder jeux en cours dans pickle ?


# On affiche les cartes existantes
print("Labyrinthes existants :")
for i, carte in enumerate(cartes):
	print("  {} - {}".format(i + 1, carte[0]))

#On demande à l'utilisateur de choisir sa carte
num_carte_choisie = input("Entrez un numéro de labyrinthe pour commencer à jouer :")

while num_carte_choisie.isdigit() is False or int(num_carte_choisie) not in range (1, len(cartes)+1):
	num_carte_choisie = input("Veuillez renseigner le numéro de la carte choisie")

#On affiche les règles et la carte
print("""
Bienvenue dans le jeu, les règles sont les suivantes.

SE REPERER
=> Les murs sont formés de la lettre 'O', vous ne pouvez pas les franchir.
=> Les portes sont symbolisées par des '.', vous pouvez les traverser.
=> Votre robot est représenté par le "X".
=> La sortie du labyrinthe est en forme de "U".

JOUER
=> 'N', 'O', 'E' et 'S' vous permettent de vous diriger respectivement au Nord, à l'Ouest, à l'Est et au Sud.
=> Pour vous déplacer de plusieurs cases en un coup, il faut préciser le nombre de cases après la direction.
Par exemple, 'E3' vous déplace de 3 cases vers l'Est.
=> 'Q' vous permet de quitter la partie en sauvegardant.

Voici votre labyrinthe !
""")

carte_choisie = Carte(cartes[int(num_carte_choisie)-1][0], cartes[int(num_carte_choisie)-1][1])
carte_en_cours = Carte(cartes[int(num_carte_choisie)-1][0], cartes[int(num_carte_choisie)-1][1])
robot = Robot(carte_choisie)
print(carte_choisie)



#On lance la boucle de jeu


should_keep_going = True

while should_keep_going is True:
	action = input("Nous vous écoutons\n").upper()

	while action[0].isalpha() is False:
		action = input("Vous devriez essayer une lettre\n").upper()

	while action[0] not in "QNOES":
		action = input("Nous ne connaissons pas cette lettre, veuillez réessayer\n").upper()
 
	if len(action) > 1:
		while action[1:].isdigit() is False:
			action = input("La drogue c'est mal, après une lettre, on met plutôt un chiffre\n").upper()
		while action[1:] == 0:
			action = input("Mais enfin vous avez bu ? Relisez les règles !\n").upper()


	#On vérifie si le déplacement est possible
	if action[0] == "N":
		robot.moveNord(action, carte_choisie, carte_en_cours)

	if action[0] == "O":
		robot.moveOuest(action, carte_choisie, carte_en_cours)

	if action[0] == "E":
		robot.moveEst(action, carte_choisie, carte_en_cours)

	if action[0] == "S":
		robot.moveSud(action, carte_choisie, carte_en_cours)

	print(carte_en_cours)

	#if action == "Q":
		#with open(chemin, "w") as fichier:
			#save & quit

	#print(robot.getposition(carte_en_cours))


	#if carte_en_cours.sortie_x == robot.x and carte_en_cours.sortie_y == robot.y:
	#	should_keep_going = False
	#	print("Félicitations, vous avez trouvé la sortie !")

	#with open(chemin, "w") as fichier:
		#save à la fin de chaque coup


