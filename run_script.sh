git clone https://github.com/ilan990/Tmdb.git
cd Tmdb
git remote remove origin
git remote add origin $GIT_TOKEN_URL
python script.py
git config --global user.email "$GIT_MAIL"
git config --global user.name "$GIT_NAME"
git add .
git commit -m "MAJ automatique"
git push --set-upstream origin master
