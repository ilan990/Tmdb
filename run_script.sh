git clone https://github.com/ilan990/Tmdb.git
cd Tmdb
ls -a
git remote remove origin
git remote add origin $GIT_TOKEN_URL
nano top_rated_movies.json
ls -a
python script.py
git config --global user.email "$GIT_MAIL"
git config --global user.name "$GIT_NAME"
git add .
git commit -m "MAJ automatique de la liste des meilleurs films"
git push --set-upstream origin master
