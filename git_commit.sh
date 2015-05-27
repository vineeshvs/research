#!bin/bash
# SAMPLE USAGE: source git_commit.sh "This is my commit message"
git init
git pull https://github.com/vineeshvs/research.git
git add *
echo "\nEnter the commit message"
echo "*************************\n"
git commit -m '$1
'
echo "\nBelow is the git status"
echo "*************************\n"
git status
echo "\nPushing to the directory  'https://github.com/vineeshvs/research.git'"
echo "***********************************************************************" 
git push https://github.com/vineeshvs/research.git
