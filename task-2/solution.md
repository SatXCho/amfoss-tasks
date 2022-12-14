Step 1:
Cloning the github repository using ```git clone https://github.com/gauthamk02/TerminalHunt.git```.

Step 2:
Creating a new directory for solutions using ```mkdir solution```.

Step 3:
Creating a text file "part1.txt" using ```touch part1.txt``` and using vim to append 107 to the text file. (107 is the atomic number of Bohrium).

Step 4:
Copying the file 1.txt from directory 06 to the solutions folder with it's name as part2.txt using the command ```cp ~/TerminalHunt/06/1.txt ~/TerminalHunt/solution/part2.txt```.

Step 5:
Accessing the git commit log using git commit with the command ```git log``` and copying the file 1.txt from directory 10 with the name part3.txt to the solutions directory.

Step 6:
Committing progress locally using ```git add .``` and ```git commit -m "gautham is a nerd"```. Additionally checking the commit status of the clone by using ```git status```.

Step 7:
Using ```git branch -a``` to see all the local and remote repositories in the repo and switching workspace to the remote branch asia using ```git checkout asia```.

Step 8:
Using ```file -name athens.txt``` to find the required file and merging the branch asia with main to access it locally using ```git merge asia```
and copying athens,txt to solutions directory with the name part4.txt.

Step 9:
Concatenating the contents of part1.txt, part2.txt, part3.txt and part4.txt into a file called password.txt in the solution directory using ```cat part1.txt part2.txt part3.txt part4.txt>password.txt```.
Removed the newline in the password.txt file using vim.

![image](https://user-images.githubusercontent.com/92297743/203363183-52f51182-f621-41da-9519-a9fc204af9e7.png)

Step 10:
To upload the solution markdown to github, I first cloned the repository using ```git clone git@github.com:SatXCho/amfoss-tasks.git```
copy the files from my working directory to the amfoss-tasks directory.
Adding the changes using ```git add .``` and committing them using ```git commit -m "gk119"```
Pushing the changes using ```git push```
