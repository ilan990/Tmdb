import os
import requests
import json
from dotenv import load_dotenv

# Chargez les variables d'environnement à partir du fichier .env
load_dotenv()
from datetime import datetime


def get_top_rated_movies(api_key, num_pages=20):
    movies = []
    for i in range(1, num_pages + 1):
        url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&page={i}'
        response = requests.get(url)
        data = response.json()
        movies.extend(sorted(data['results'], key=lambda x: x['vote_average'], reverse=True))
    return movies


def save_movies_to_json(movies, filename):
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(movies, json_file, ensure_ascii=False, indent=4)


def load_movies_from_json(filename):
    print(f"Lecture du fichier JSON '{filename}'")
    with open(filename, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    print("Lecture terminée avec succès.")
    return data


def send_sms(message):
    try:
        response = requests.get(os.environ.get('URL') + f'user={os.environ.get("FREE_USER")}&pass={os.environ.get("FREE_API_KEY")}&msg={message}')
        if response.status_code == 200:
            print('Le message a bien été envoyé')
        else:
            print('Échec de l\'envoi')
    except Exception as e:
        print(f'Une erreur est survenue : {e}')


def main():
    # Remplacez 'VOTRE_CLE_API' par votre clé d'API TMDb
    api_key = os.environ.get('TMDB_API_KEY')

    # Obtenir les nouveaux films
    new_movies = get_top_rated_movies(api_key)

    # Charger les anciens films depuis le fichier JSON
    old_movies = load_movies_from_json('top_rated_movies.json')

    # Identifier les nouveaux films
    new_movie_ids = set([film['id'] for film in new_movies])
    old_movie_ids = set([film['id'] for film in old_movies])
    new_ids = new_movie_ids - old_movie_ids

    # Obtenir les détails des nouveaux films
    new_movies_data = [film for film in new_movies if film['id'] in new_ids]

    # Liste pour stocker les titres des nouveaux films
    new_movie_titles = [film['title'] for film in new_movies_data]

    # Envoyer un SMS avec les titres des nouveaux films
    if new_movies_data:
        message = f"Coucou c'est IlanGPT, il y a du nouveau dans le top des films: {', '.join(new_movie_titles)}"
        send_sms(message)

    # Enregistrer les nouveaux films dans un fichier JSON
    save_movies_to_json(new_movies, 'top_rated_movies.json')

if __name__ == '__main__':
    main()