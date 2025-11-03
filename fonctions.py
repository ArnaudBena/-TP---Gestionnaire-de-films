import csv
import os

def ajouter_film():
    """
    Demande les informations à l’utilisateur et ajoute un film dans le fichier CSV
    """
    with open("films.csv", "r", encoding="utf-8")as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    titres_existants = [film["titre"].lower() for film in rows]

    while True:
        titre = input("🎞️  Titre du film : ")
        if titre in titres_existants:
            print("Ce film est déjà dans la liste ")
            continue
        if titre.lower() == "q":
            return
        annee = input(f"Année de sortie du film {titre} : ")
        if annee.lower() == "q":
            return
        genre = input(f"Genre du film {titre} : ").upper()
        if genre.lower() == "q":
            return
        vu = input("Avez-vous vu ce film ? Oui ou Non : ").lower()
        if vu.lower() == "q":
            return
        with open("films.csv", "a", newline="", encoding="utf-8") as fichier:
            champs = ["titre", "année", "genre", "vu"]
            writer = csv.DictWriter(fichier, fieldnames=champs)
            writer.writerow({"titre": titre, "année": annee, "genre": genre, "vu": vu})
        print(f"\n✅ Le film « {titre} » a été ajouté à votre gestionnaire de film.\n")
        menu()

def afficher_films():
    """
    Affiche joliment la liste des films présents dans le fichier CSV.
    Si aucun film n’est trouvé, un message s’affiche.
    """
    os.system("cls")
    with open("films.csv", "r", encoding="utf-8")as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("Aucun contact pour le moment.")
    else:
        print("\n🎞️  Liste des films enregistrés :\n")
        for film in rows:
            print(f"- {film['titre']} ({film['année']}) | Genre : {film['genre']} | Vu : {film['vu']}")

# 1️⃣ Rechercher un film
#    - Demander à l’utilisateur un titre à chercher.
#    - Lire le CSV et parcourir la liste de films.
#    - Comparer en ignorant la casse.
#    - Si trouvé : afficher toutes les infos du film.
#    - Sinon : afficher un message clair “Film non trouvé”.
#    - Prévoir la possibilité de quitter la recherche (saisie “q”).

def rechercher_films():
    pass
















def quitter():
    """
    Fonction pour quitter le programme, gère aussi le cas ou on ne mets pas Oui ou Non 
    """
    while True:
        choix = input("Êtes vous sur de vouloir quitter (Oui / Non) : ")
        if choix.lower() == "oui":
            print("Merci d'avoir jouer à bientot 👋 ")
            exit()
        elif choix.lower() == "non":
            menu()
        else:
            print("❌ Veuillez faire un choix parmis ceux disponnible ❌")

def menu():
    """
    Fonction qui gère l'affichage du menu et lance les programmes voulus
    """
    while True:
        os.system("cls")
        choix = input(" \n Que voulez-vous faire :\n 1- Ajouter un film \n 2- Afficher un film \n 3- Supprimer \n 4- Quitter \n Votre choix : ")
        if choix == "1":
            ajouter_film()
        elif choix == "2":
            afficher_films()
        elif choix == "3":
            pass
        elif choix == "4":
            quitter()
        else:
            print("❌ Veuillez faire un choix parmis ceux disponnible ❌")
            continue




menu()