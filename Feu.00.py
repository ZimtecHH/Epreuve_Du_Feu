largeur = int(input("rentrez la largueur : "))
hauteur = int(input("rentrez la hauteur : "))

if largeur <= 0 or hauteur <= 0:
    print("erreur d'argument, la largeur et la hauteur doivent être supérieures à zéro.")
    exit()

#afficher une ligne complète
def afficher_ligne():
    print(f"o{(largeur-2)*'-'}o")

if hauteur == 1:
    afficher_ligne()
else:
    #nombre de ligne = hauteur - 2
    def nombre_de_ligne():
        print(f"|{(largeur-2) * ' '}|")

    afficher_ligne()

    for i in range(hauteur-2):
        nombre_de_ligne()

    afficher_ligne()
