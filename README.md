#Make a shell script called autoGit.sh with the following code inside it:
#!/usr/bin/sh

touch README.md
git init
git add README.md
git commit -n "Added"
hub create
git push -u origin master
