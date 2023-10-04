# Projet Tmdb Automatisé
Ce projet automatisé utilise un script Python pour récupérer les derniers films les mieux notés depuis l'API TMDb, les compare avec la version précédente, envoie un SMS si de nouveaux films sont trouvés, et met à jour le fichier JSON local.

## Fonctionnement
Le script script.py est déclenché automatiquement chaque jour grâce à une configuration sur Heroku. Voici comment cela fonctionne :

**Récupération des Films**: Le script utilise l'API TMDb pour récupérer les films les mieux notés.

**Comparaison des Films**: Les nouveaux films sont comparés avec la version précédente pour détecter les ajouts.

**Notification SMS**: Si de nouveaux films sont trouvés, le script envoie un SMS contenant les titres des nouveaux films.

**Mise à Jour du Fichier JSON**: Les nouveaux films sont enregistrés dans le fichier **top_rated_movies.json** pour la prochaine comparaison.

## Configuration
**API TMDb**: Assurez-vous d'avoir une clé d'API TMDb valide et configurez-la dans votre environnement sous le nom TMDB_API_KEY.

**SMS Notification**: Configurez les variables d'environnement URL, **FREE_USER** et **FREE_API_KEY** pour l'envoi de SMS.

**Git Configuration**: Configurez les variables d'environnement **GIT_TOKEN_URL**, **GIT_MAIL** et **GIT_NAME** pour l'authentification Git.

## Configuration d'Automatisation
Ce projet utilise Heroku pour l'automatisation. Le fichier **Procfile** spécifie la commande à exécuter : **web: bash run_script.sh**. Le script **run_script.sh** effectue les étapes nécessaires pour récupérer les données, les comparer et envoyer un SMS le cas échéant.

## Dépendances
Ce projet utilise la bibliothèque Python **requests** pour effectuer des requêtes HTTP. Assurez-vous d'installer les dépendances en exécutant :

```pip install -r requirements.txt```
## Exécution Manuelle
Si vous souhaitez exécuter le script manuellement, assurez-vous d'ajouter les variables d'environnement nécessaires et exécutez **script.py**.

```python script.py```
