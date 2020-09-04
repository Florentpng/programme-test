terminal = True
print("")

while terminal == True:
	prenom = input("Quel est votre prénom ?")
	print("")
	texte = ("Bonjour {}, Les menus sont :")
	print(texte.format(prenom))

	print("")
	print("- calcul (permet de faire des calculs basiques)")
	print("")
	print("- age (donne une information sur votre age)")
	print("")
	print("- repeat (répétition d'un mot)")
	print("")
	print("- quit (quitte le programme)")
	print("")

	menu = input("Dans quel menu voulez vous aller ? ")
	print("")

	if menu == "age":
		""" Tentative d'une boucle avec un affichage d'erreur, sans succès...
		erreur = False
		while erreur == False:
			age = input("Quel age avez vous ? ")
			try:
				age = int(age)
			except ValueError:
				print("")
				print("Vous devez entrer un nombre entier !")
				print("")
			finally:
				erreur = True
		"""
		age = input("Quel age avez vous ?")
		age = int(age)
		if age <= 0:
			print("")
			print('Vous n\'êtes pas encore né ')
			print("")
		elif 0 < age < 18:
			print("")
			print('vous êtes mineur ')
			print("")
		elif 18 <= age <= 100:
			print("")
			print('Vous êtes majeur ')
			print("")
		else:
			print("")
			print('Vous êtes mort ')
			print("")

	elif menu == "repeat":
		mot = input("Quel mot voulez vous répeter ? ")
		i = 0
		while i < 5:
			print(mot)
			i += 1

	elif menu == "quit":
		break

	elif menu == "calcul":

		premier = input("Quel est le premier nombre ? ")
		try:
			premier = float(premier)
		except ValueError:
			print("")
			print("Vous devez entrer un nombre !")
			print("")
		else:
			second = input("Quel est le second nombre ? ")
			try:
				second = float(second)
			except ValueError:
				print("")
				print("Vous devez entrer un nombre !")
				print("")
			else:
				signe = input("Quel est le mode opératoire ? (+ - / * %) ")
				print("")
				if signe == "+":
					print(premier + second)
				elif signe == "-":
					print(premier - second)
				elif signe == "/":
					print(premier / second)
				elif signe == "*":
					print(premier * second)
				elif signe == "%":
					print(premier % second)
				else:
					print("")
					print("Mode opératoire incorrect !")
					print("")

	else:
		print("")
		print("Menu incorrect")
		print("")

print("A bientôt")