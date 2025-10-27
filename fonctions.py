import csv

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
        if titre.lower() in titres_existants:
            print("Ce film est déjà dans la liste ")
            continue
        if titre.lower() == "q":
            return
        annee = input("Année de sortie : ")
        if annee.lower() == "q":
            return
        genre = input("Genre : ")
        if genre.lower() == "q":
            return
        vu = input("Avez-vous vu ce film ? (oui/non) : ")
        if vu.lower() == "q":
            return
        with open("films.csv", "a", newline="", encoding="utf-8") as fichier:
            champs = ["titre", "année", "genre", "vu"]
            writer = csv.DictWriter(fichier, fieldnames=champs)
            writer.writerow({"titre": titre, "année": annee, "genre": genre, "vu": vu})
        print(f"\n✅ Le film « {titre} » a été ajouté à votre collection.\n")

def afficher_films():
    """
    Affiche joliment la liste des films présents dans le fichier CSV.
    Si aucun film n’est trouvé, un message s’affiche.
    """
    with open("films.csv", "r", encoding="utf-8")as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("Aucun contact pour le moment.")
    else:
        print("\n🎞️  Liste des films enregistrés :\n")
        for film in rows:
            print(f"- {film['titre']} ({film['année']}) | Genre : {film['genre']} | Vu : {film['vu']}")

ajouter_film()
afficher_films()