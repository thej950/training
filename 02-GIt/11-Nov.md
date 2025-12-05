# Branching 

## Main branch-CodeOwner Machine Commands
 
  481  # fetch ,merge and pull
  482  # consider there is a new file added in the remote repo which is github repo, with the help of fetch command you can decide that these commits which are on remote system are to be merged in the local repo or not if you want to merge then we use merge command
  483  ls
  484  ls
  485  git fetch
  486  ls
  487  git merge origin/main
  488  ls
  489  git status
  490  git log --oneline
  491  # git pull command combination of fetch + merge
  492  ls
  493  git pull origin main
  494  ls
  495  git log --oneline
  496  # Best Practices...First Pull and then push the code
  497  history
  498  git branch
  499  git log --oneline
  500  # Whenever a developer joins the project then first we will create the branch for that developer so so that we can seprate out dev1 code from other developer
  501  # Consider there are 2 developers Dev1 and Dev2 joins your project, so it means the code owner will create 2 branches one for Dev1 and Second for Dev2
  502  # To create for developers the branch on codeowner machine we use git branch <branchname > command
  503  git branch Dev1
  504  git branch
  505  # To delete the branch git branch -D <branch name>
  506  git branch -D Dev1
  507  git branch
  508  git branch Dev1
  509  git branch Dev2
  510  # So far the Dev1 and Dev2 branches are on local system of code owner and to share with dev1 & dev2 we need to push the code in Github branches(dev1 and Dev2)
  511  git push origin Dev1
  512  git push origin Dev2
  513  # now Dev1 wants to download the code from Dev1 branch for that we will use git clone with branch name git clone -b <branchname> <repourl>
  514  ls
  515  git pull origin main
  516  ls
  517  git log --oneline
  518  ls
  519  git checkout Dev1
  520  git branch
  521  ls
  522  git pull origin Dev1
  523  ls
  524  git checkout -
  525  git checkout Dev2
  526  ls
  527  git pull origin Dev2
  528  ls
  529  git checkout -
  530  git merge Dev2
  531  ls


## Dev1 machine commands
 
  498  # I am on Dev1 laptop
  499  git clone -b Dev1 https://github.com/onlineTrainingguy/AIProject.git
  500  cd AIProject/
  501  ls
  502  git log --onelin
  503  git branch
  504  ls
  505  touch Dev1.java
  506  ls
  507  git status
  508  git add Dev1.java
  509  git config --local user.name dev1
  510  git config --local user.email dev1@gmail.com
  511  git commit -m "Dev1.java file is added by Dev1 user"
  512  git push origin Dev1
  513  git push origin main

## Dev2 machine commands
 
  498  # I am on Dev2 machine

  499   git clone -b Dev2 https://github.com/onlineTrainingguy/AIProject.git

  500  cd AIProject/

  501  git branch

  502  ls

  503  touch Dev2.java

  504  git status

  505  git add .

  506  git commit -m "Dev2.java file is added by Dev2"

  507  git status

  508  git config user.name dev2

  509  git config user.email dev2@gmail.com

  510  git commit -m "Dev2.java file is added by Dev2"

  511  git push origin Dev2

# Merge Conflict
 
  549  #Merge Conflict...Dev1 and Dev2 working on same file and their code is to be merged into main branch

  550  git branch

  551  git checkout dev1

  552  git branch

  553  git checkout -

  554  git checkout Dev1

  555  ls

  556  cat AI.java

  557  echo "AI.java file modified by Dev1" > AI.java

  558  git commit -am "Dev1 Code for AI.java"

  559  cat AI.java

  560  git log --oneline

  561  git checkout Dev2

  562  cat AI.java

  563  echo "AI.java file modified by Dev2" > AI.java

  564  git commit -am "Dev2 Code for AI.java"

  565  cat AI.java

  566  git checkout main

  567  cat AI.java

  568  git merge Dev1

  569  cat AI.java

  570  git merge Dev2

  571  ls

  572  cat AI.java

  573  gitmergetool

  574  cat AI.java

  575  git status

  576  git add .

  577  git commit -m "AI.java merge conflict is resolved"

  578  git status

  579  git checkout Dev1

  580  cat AI.java

  581  git merge main

  582  cat AI.java

  583  git checkout Dev2

  584  cat AI.java

  585  git merge main

  586  cat AI.java

  587  git push origin Dev2

  588  git checkout -

  589  git push origin Dev1

  590  git checkout main

  591  git push origin main



# Git merge and Rebase

  594  cd ..

  595  mkdir mr

  596  cd mr/

  597  touch m1 m2 m3

  598  git init

  599  git status

  600  git add .

  601  git status

  602  git commit -m "m1" m1

  603  git commit -m "m1" m2

  604  git reset --soft HEAD~1

  605  git log

  606  git status

  607  git commit -m "m2" m2

  608  git commit -m "m3" m3

  609  git status

  610  git branch feature

  611  git checkou feature

  612  git checkout feature

  613  touch f1

  614  git commit -am "f1"

  615  git commit -am "f1" f1

  616  git add .

  617  git commit -m "f1"

  618  git log --oneline

  619  git checkout -

  620  touch m4

  621  git add .

  622  git commit -m "m4"

  623  git checkout -

  624  ls

  625  git merge master

  626  git log --oneline

  627  git reset --hard HEAD~2

  628  git log --oneline

  629  git checkout -

  630  ls

  631  git log --oneline

  632  git reset --hard HEAD~1

  633  ls

  634  git checkout -

  635  ls

  636  touch f1

  637  git add .

  638  git commit -m "f1"

  639  git checkout -

  640  touch m4

  641  git add .

  642  git commit -m "m4"

  643  git log --oneline

  644  git checkout feature

  645  git rebase master

  646  ls

  647  git log --oneline

 
# Stash Command

  650  # consider you are reviewing the code of branch and until you commit this code in your local system this uncommited code is visible in all the branches

  651  ls

  652  echo "Testing f1 code" > f1

  653  ls

  654  cat f1

  655  git checkout -

  656  git add .

  657  ls

  658  git status

  659  git checkout -

  660  git stash save "f1 file is stashed"

  661  ls

  662  cat f1

  663  git checkout -

  664  git checkout -

  665  ls

  666  git stash list

  667  git stash pop

  668  ls

  669  cat f1

  670  git status

  671  git add .

  672  git stash save "f1 is in stashed area"

  673  touch f2

  674  git add .
s
  675  git stash "f2 is in the stash area"

  676  touch f3

  677  git add .

  678  git stash "f3 is stashed"

  679  git stash save "f3 is stashed"

  680  git stash list

  681  ls

  682  git stash clear

  683  git stash list

  684  ls

  685  cat f1

  686  echo "f1 is modified" > f1

  687  git add .

  688  git stash save "f1"

  689  git stash list

  690  touch f2

  691  git add .

  692  ls

  693  git stash save "f2"

  694  git stash list

  695  touch f3

  696  git add .

  697  git stash "f3"

  698  git stash list

  699  git stash save "f3"

  700  git stash list

  701  # 1. to bring back from stash to stage/untracked area on the basis of index number then we can use pop

  702  #2 keep the changes in stash as well as in the working copy (git stash apply)

  703  #3 to remove the entries in stash and donot copy back to stag/untracked area drop(index) or clear- remove all stashes

  704  git stash list

  705  git stash apply{0}

  706  git stash apply stash@{0}

  707  git status

  708  git stash list

  709  git stash drop stash@{0}

  710  git stash list

  711  git stash pop stash@{0}

  712  git status


# git Tags
 
714  cd ..

  715  cd AI\ Project/

  716  ls

  717  git tag v1

  718  git tag

  719  touch v2.java v21.java

  720  git add .

  721  git commit -m "version 2 of project is released"

  722  git tag v2

  723  git tag

  724  touch v3.java v31.java

  725  git add .

  726  git commit -m "Version 3 is released"

  727  git tag v3

  728  git log --oneline

  729  ls

  730  git checkout v1

  731  ls

  732  git checkout v2

  733  ls

  734  git checkout v3

  735  ls

  736  git checkout main

  737  git push --tags

 