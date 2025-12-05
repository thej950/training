# Git - it is a DVCS Developed by Linus Torvalds 
 - Git has three stages WS -> STG-> Committed STG 
 - local and global cofigurations 
    $ git config --global user.name abcuser
    $ git config --global user.email abcuser@gmail.com 
 - Now automatically a .global file will be created 

# Working on files in Local Repo 
    498  git --version
    499  touch AI.java
    500  touch NoteLM.java
    501  touch GenerativeAI.java
    502  git init
    503  git status
    504  git add AI.java
    505  git status
    506  git rm --cached AI.java
    507  git status
    508  git add -A
    509  git status
    510  # Before commit the code we need to define the author name and author email
    511  # with configuration, Global configuragtion(on laptop users/.gitconfig), Local Configuration(DevBox .git/config)
    512  # let's define the author name and email in the .git config file using global configuration
    514  git config --global user.name globaluser
    515  git config --global user.email globaluser@gmail.com
    516  git status
    517  git commit -m "AI.java file is added to local Repo"
    518  git status
    519  # to check all the commits you can use git log command
    520  git log
    521  git config --local user.name localuser
    522  git status
    523  git commit -m "GenerativeAI.java and NoteLM.java files are added and author is localuser"
    524  git log
    525  git status

# Token creation 
```bash
  Open GitHub -> Goto Profile -> Developer settings -> Personnel access tokens -> tokens(classic) -> Generate a new token -> Generate a new classic token  
```
 - permission use only 
   - repo(select)
   - admin:org(select) 
 - store it for future use case  


# pushing into Github repo 

527  git remote add origin https://github.com/onlineTrainingguy/AIProject.git
  528  git branch
  529  git branch -M main
  530  # Whatever is in the main branch of local Repo i want to push to remote Github AIProject Repo
  531  git push -u origin main
  532  git push -u origin main
  533  git push -u origin main
  534  git log --oneline


# .gitignore

536  # .gitignore file is the file where we keep the file name which are in the current directory but we donot want to track those changes...eg logfiles,executable
  537  touch 1.exe 2.exe 3.log 4.log
  538  ls
  539  git status
  540  vi .gitignore
  541  git status
  542  vi .gitignore
  543  git status
  544  ls
  545  cat .gitignore
  546  rm *.exe *.log .gitignore

# reset (soft,hard,mixed), revert 
548  # commit means a snapshot ( a file which stores the code changes which you have commited)
549  # if commit get deleted then the snapshot is also deleted and you can not recover the changes
550  # .git which is local repo folder and if this folder is deleted then your entire repo is deleted
551  # git reset command- it will delete the commit , options --mixed default option( goes into untracked) , --soft (goes into stage area), -- hard (permanently deletes the commit)
552  # git reset deletes the recent commits means if you want to delete the commit which is last 3rd commit then you need to delete all the commits which are after that (second last and last commit)
553  touch tmp.java
554  ls
555  git status
556  git add .
557  git commit -m "tmp.java file is added"
558  git log --oneline
559  git reset HEAD~1
560  git log --oneline
561  git status
562  git add .
563  git status
564  git commit -m "tmp.java file is added in the repo"
565  git log --oneline
566  git reset --soft HEAD~1
567  git log --oneline
568  git status
569  git commit -m "tmp.java file is added"
570  git log --oneline
571  git reset --hard HEAD~1
572  git log --oneline  573  git status
574  ls
575  # revert command is to revert back the changes without deleteing the commits, whenever we are reverting the changes then it basically creates a new commit for the revert back changes(snapshot)
576  # I will create a appsettins.json file and add some data into this file and then we will do the revert back
577  # create a appsettings.json file
578  touch appsettings.json
579  ls
580  git status
581  git add .
582  git commit -m "appsettings.json file is added"
583  git log--oneline
584  git log --oneline
585  # add some content to my file
586  echo "{name:git}" > appsettings.json
587  cat appsettings.json
588  git status
589  git commit -m "appsettings.json file is updated"
590  git commit -am "appsettings.json file is updated"
591  git log --online
592  git log --oneline
593  cat appsettings.json
594  # now let's use the revert command to delete the content of appsettings.json file
595  git log --oneline
596  git diff 6fbed14 1e4ca37
597  git revert 6fbed14
598  cat appsettings.json
599  git log --oneline
600  git revert 8ecf347
601  cat appsettings.json
602  git log --oneline
603  git reset --hard HEAD~4
604  git log --oneline
605  ls


# github sync (Pull, push, fetch, merge)

  607  # fetch ,merge and pull
  608  # consider there is a new file added in the remote repo which is github repo, with the help of fetch command you can decide that these commits which are on remote system are to be merged in the local repo or not if you want to merge then we use merge command
  609  ls
  610  ls
  611  git fetch
  612  ls
  613  git merge origin/main
  614  ls
  615  git status
  616  git log --oneline
  617  # git pull command combination of fetch + merge
  618  ls
  619  git pull origin main
  620  ls
  621  git log --oneline
  622  # Best Practices...First Pull and then push the code
