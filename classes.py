
# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""

class Carte:

	"""Objet de transition entre un fichier et un labyrinthe."""

	def __init__(self, nom, lignes):
		self.nom = nom
		self.lignes = list(lignes)
		self.getsortie()

	def __repr__(self):
		return "<Carte {}>".format(self.nom)

	def __str__(self):
		lignes = self.lignes
		return "\n".join(self.lignes)

	def getsortie(self):
		for i, ligne in enumerate(self.lignes):
			if "U" in ligne:
				self.sortie_x = ligne.index("U")
				self.sortie_y = i
		

class Robot:
	def __init__(self, carte):
		self.getposition(carte)

	def getposition(self, carte):
		for i, ligne in enumerate(carte.lignes):
			if "X" in ligne:
				self.x = ligne.index("X")
				self.y = i
		return self.x, self.y

	def moveNord(self, action, carte_choisie, carte_en_cours):
		if len(action) == 1:
			action = "N1"
		if int(action[1:]) <= self.y:
			for i in range(1, int(action[1:]) + 1):
		
				#SI ON VA SUR "O"
				if carte_choisie.lignes[self.y-i][self.x] == "O" :
					print("Vous entrez dans un mur, vous ne pouvez pas effectuer ce déplacement")
					return
				
			#SI ON VA SUR " " ou "." ou "U"
			if carte_choisie.lignes[self.y-int(action[1:])][self.x] in " .U":
				
				#SPECIFIQUE SI ON VA SUR "U"
				if carte_choisie.lignes[self.y-int(action[1:])][self.x] == "U" :
					print("Félicitations, vous avez atteint la sortie !")

				#SI ON EST SUR " " OU "X"
				if carte_choisie.lignes[self.y][self.x] in " X":
					carte_en_cours.lignes[self.y] = carte_en_cours.lignes[self.y].replace("X", " ")
		
				#SI ON EST SUR "." 
				elif carte_choisie.lignes[self.y][self.x] == ".":
					carte_en_cours.lignes[self.y] = carte_choisie.lignes[self.y]

				self.y -= int(action[1:])
				carte_en_cours.lignes[self.y] = carte_en_cours.lignes[self.y][:self.x] + "X" + carte_en_cours.lignes[self.y][int(self.x+1):]
		
		else:
			print("Vous ne pouvez pas effectuer ce déplacement.\nLe Cours Préparatoire vous apprend à compter, n'hésitez pas à y refaire un tour ;)")

	def moveOuest(self, action, carte_choisie, carte_en_cours):
		if len(action) == 1:
			action = "O1"
		if int(action[1:]) <= self.x:
			for i in range(1, int(action[1:]) + 1):
		
				#SI ON VA SUR "O"
				if carte_choisie.lignes[self.y][self.x-i] == "O" :
					print("Vous entrez dans un mur, vous ne pouvez pas effectuer ce déplacement")
					return

			#SI ON VA SUR " " ou "." ou "U"
			if carte_choisie.lignes[self.y][self.x-int(action[1:])] in " .U":

				#SPECIFIQUE SI ON VA SUR "U"
				if carte_choisie.lignes[self.y][self.x-int(action[1:])] == "U" :
					print("Félicitations, vous avez atteint la sortie !")

				#SI ON EST SUR " " OU "X"
				if carte_choisie.lignes[self.y][self.x] in " X":
					carte_en_cours.lignes[self.y] = carte_en_cours.lignes[self.y].replace("X", " ")

				#SI ON EST SUR "."
				elif carte_choisie.lignes[self.y][self.x] == ".":
					carte_en_cours.lignes[self.y] = carte_choisie.lignes[self.y]
				
				self.x -= int(action[1:])
				carte_en_cours.lignes[self.y] = carte_en_cours.lignes[self.y][:self.x] + "X" + carte_en_cours.lignes[self.y][int(self.x+1):]

		else:
			print("Vous ne pouvez pas effectuer ce déplacement.\nLe Cours Préparatoire vous apprend à compter, n'hésitez pas à y refaire un tour ;)")

	def moveEst(self, action, carte_choisie, carte_en_cours):
		if len(action) == 1:
			action = "E1"
		if int(action[1:]) <= int((len(carte_en_cours.lignes[self.x])-1)) - int(self.x):
			for i in range(1, int(action[1:]) + 1):

				#SI ON VA SUR "O"
				if carte_choisie.lignes[self.y][self.x+i] == "O" :
					print("Vous entrez dans un mur, vous ne pouvez pas effectuer ce déplacement")
					return

			#SI ON VA SUR " " ou "." ou "U"
			if carte_choisie.lignes[self.y][self.x+int(action[1:])] in " .U":

				#SPECIFIQUE SI ON VA SUR "U"
				if carte_choisie.lignes[self.y][self.x+int(action[1:])] == "U" :
					print("Félicitations, vous avez atteint la sortie !")

				#SI ON EST SUR " " OU "X"
				if carte_choisie.lignes[self.y][self.x] in " X":
					carte_en_cours.lignes[self.y] = carte_en_cours.lignes[self.y].replace("X", " ")

				#SI ON EST SUR "."
				elif carte_choisie.lignes[self.y][self.x] == "." :
					carte_en_cours.lignes[self.y] = carte_choisie.lignes[self.y]
					
				self.x += int(action[1:])
				carte_en_cours.lignes[self.y] = carte_en_cours.lignes[self.y][:self.x] + "X" + carte_en_cours.lignes[self.y][int(self.x+1):]

		else:
			print("Vous ne pouvez pas effectuer ce déplacement.\nLe Cours Préparatoire vous apprend à compter, n'hésitez pas à y refaire un tour ;)")

			

	def moveSud(self, action, carte_choisie, carte_en_cours):
		if len(action) == 1:
			action = "S1"
		if int(action[1:]) <= (len(carte_en_cours.lignes)-1) - self.y:
			for i in range(1, int(action[1:]) + 1):

				#SI ON VA SUR "O"
				if carte_choisie.lignes[self.y+i][self.x] == "O" :
					print("Vous entrez dans un mur, vous ne pouvez pas effectuer ce déplacement")
					return

			#SI ON VA SUR " " OU "." ou "U"
			if carte_choisie.lignes[self.y+int(action[1:])][self.x] in " .U":

				#SPECIFIQUE SI ON VA SUR "U"
				if carte_choisie.lignes[self.y+int(action[1:])][self.x] == "U" :
					print("Félicitations, vous avez atteint la sortie !")

				#SI ON EST SUR " " OU "X"
				if carte_choisie.lignes[self.y][self.x] in " X":
					carte_en_cours.lignes[self.y] = carte_en_cours.lignes[self.y].replace("X", " ")
					
				#SI ON EST SUR "."
				elif carte_choisie.lignes[self.y][self.x] == ".":
					carte_en_cours.lignes[self.y] = carte_choisie.lignes[self.y]
				
				self.y += int(action[1:])
				carte_en_cours.lignes[self.y] = carte_en_cours.lignes[self.y][:self.x] + "X" + carte_en_cours.lignes[self.y][int(self.x+1):]

		else:
			print("Vous ne pouvez pas effectuer ce déplacement.\nLe Cours Préparatoire vous apprend à compter, n'hésitez pas à y refaire un tour ;)")