import csv
import os

# Chemins vers le fichier CSV utilisé pour sauvegarder les films
CSV_FILE_PATH = "films.csv"
FIELD_NAMES = ["titre", "année", "genre", "vu"]

def save_csv(data: dict):
    """
    Cette fonction enregistre la liste de dictionnaire 'data' dans le csv configuré dans 'CSV_FILE_PATH'
    ⚠️ **Attention** : Cette fonction écrase le contenu CSV existant.
    """
    formatted_data = []
    for film in data:
        formatted_data.append({
            **film,
            'vu': 'oui' if film['vu'] else 'non'
        })

    with open(CSV_FILE_PATH, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
        writer.writeheader()
        writer.writerows(formatted_data)

def load_csv() -> dict:
    """
    Cette fonction va lire le fichier CSV et retourner son contenu sous forme de dictionnaire.
    """
    if not os.path.exists(CSV_FILE_PATH):
        return []
    
    with open(CSV_FILE_PATH, "r", encoding="utf-8", newline="") as file:
        data = []
        reader = csv.DictReader(file)
        for film in reader:
            data.append({
                'titre': film['titre'],
                'année': int(film['année']),
                'genre': film['genre'],
                'vu': film['vu'] == 'oui'
            })
        return data
