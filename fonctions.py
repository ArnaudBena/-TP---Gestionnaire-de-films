import csv
from csvmanager import *
import Levenshtein 

def ajouter_film():
    """
    Demande les informations à l’utilisateur et ajoute un film dans le fichier CSV
    """
    with open("films.csv", "r", encoding="utf-8", newline="")as f:
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
        genre = input(f"Genre du film {titre} : ")
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
    with open("films.csv", "r", encoding="utf-8")as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("Aucun film pour le moment.")
    else:
        print("\n🎞️  Liste des films enregistrés :\n")
        for film in rows:
            print(f"- {film['titre']} ({film['année']}) | Genre : {film['genre']} | Vu : {film['vu']}")


def rechercher_films():
    films = load_csv()
    query = input("Entrez le mot clé à rechercher : ")

    for film in films:
        dst = Levenshtein.distance(film['titre'], query)
        is_partial_match = query.lower().strip() in film['titre'].lower()
        is_approx_match = dst <= 3
        if is_partial_match or is_approx_match:
            print(f"- {film['titre']} ({film['année']}) | Genre : {film['genre']} | Vu : {film['vu']}")

def supprimer_film():
    films = load_csv()
    query = input("Entrez le titre du film à supprimer : ").strip()

    for film in films.copy():
        if query.lower() == film['titre'].lower():
            films.remove(film)
            print(f"{film['titre']} a bien été supprimé !")
    
    save_csv(films)

def marquer_vu():
    films = load_csv()
    query = input("Quel film voulez-vous marquer comme vu ? ").strip()

    for film in films:
        if query.lower() == film['titre'].lower():
            if film['vu'] == True:
                print("Ce film a déjà été Vu")
            else:
                film['vu'] = True
                print(f"Merci d'avoir regardé le film {film['titre']}")
    save_csv(films)


def quitter():
    """
    Fonction pour quitter le programme, gère aussi le cas ou on ne mets pas Oui ou Non 
    """
    while True:
        choix = input("Êtes vous sur de vouloir quitter (Oui / Non) : ")
        if choix.lower() == "oui":
            print("Merci d'avoir utilisé le gestionnaire de film et à bientot 👋 ")
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
        choix = input(" \n Que voulez-vous faire :\n 1- Ajouter un film \n 2- Afficher un film \n 3- Rechercher un Film \n 4- Supprimer un Film \n 5- Marquer Vu \n 6- Quitter \n Votre choix : ")
        if choix == "1":
            ajouter_film()
        elif choix == "2":
            afficher_films()
        elif choix == "3":
            rechercher_films()
        elif choix == "4":
            supprimer_film()
        elif choix == "5":
            marquer_vu()
        elif choix == "6":
            quitter()
        else:
            print("❌ Veuillez faire un choix parmis ceux disponnible ❌")
            continue
