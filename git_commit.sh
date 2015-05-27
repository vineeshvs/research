#!bin/bash
# SAMPLE USAGE: source git_commit.sh "This is my commit message"
git init
git pull https://github.com/vineeshvs/research.git
git add *
echo "\nENTER COMMIT MESSAGE"
echo "*************************\n"
read commit_message
git commit -m '$commit_message'
echo "\n\nGIT STATUS\n\n"
echo "*************************\n"
git status
echo "\nPUSING INTO THE DIRECTORY  'https://github.com/vineeshvs/research.git'\n"
echo "***********************************************************************" 
git push https://github.com/vineeshvs/research.git
#set prompt ":|#|\\\$"
#set prompt "Username for 'https://github.com': "
#interact -o -nobuffer -re $prompt return
#send "vineeshvs\r"
#interact -o -nobuffer -re $prompt return
#send "vineeshvs6\r" 
