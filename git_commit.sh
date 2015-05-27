#!bin/expect
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
autoexpect "Username for 'https://github.com':"
send "vineeshvs"
autoexpect "Password for 'https://vineeshvs@github.com':"
send "vineeshvs6"
