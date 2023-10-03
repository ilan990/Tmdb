GIT_REPO_PATH=$(pwd)

# Assurez-vous d'être dans le bon répertoire
cd $GIT_REPO_PATH
git pull origin master

python script.py
git add .
git commit -m "MAJ automatique"
git push origin master