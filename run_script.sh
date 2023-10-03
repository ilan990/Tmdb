cd $GIT_REPO_PATH
git pull origin master
python script.py
git add .
git commit -m "MAJ automatique"
git push origin master