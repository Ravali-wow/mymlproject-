PS D:\mymlproject> git init
Reinitialized existing Git repository in D:/mymlproject/.git/
PS D:\mymlproject> git add README.md
fatal: pathspec 'README.md' did not match any files
PS D:\mymlproject> conda activate venv/
PS D:\mymlproject> git init            
Reinitialized existing Git repository in D:/mymlproject/.git/
PS D:\mymlproject> git add README.md   
fatal: pathspec 'README.md' did not match any files
PS D:\mymlproject> git add README.md
fatal: pathspec 'README.md' did not match any files
PS D:\mymlproject> git add README.md
fatal: pathspec 'README.md' did not match any files
PS D:\mymlproject> git add README.md
fatal: pathspec 'README.md' did not match any files
PS D:\mymlproject> git add README.md
PS D:\mymlproject> git commit -m "First commit"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'mycutie@ravali.(none)')
PS D:\mymlproject> git config --global user.email "kanduriravali@gmail.com"
PS D:\mymlproject> git config --global user.name "Ravali-wow"
PS D:\mymlproject> git commit -m "First commit"
[master (root-commit) 02363fc] First commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README.md
PS D:\mymlproject> 
__init__.py is to identify a particular folder
python setup.py bdist_egg ---------- command to generate .egg-info file for our project

python -m src.exception_handler ---------- to run a file present in src package

#To push our local repo to remote git server.
1.git add . ----------------adds to git
2.git push origin main------------to push from origin of repository to main repository present in git hub server
3.git commit -m "CommitName"-------------it commits the pushed repo in git server


#To download a library 
1,add that requirement in requirements.txt
2.run 'pip install -r requirements.txt'

#To upgrade pip or install latest version of pip
1. run 'python -m pip install --upgrade pip'

#Got this error
conda : The term 'conda' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the 
spelling of the name, or if a path was included, verify that the path is correct and try again
  --resolved this by adding bin and Scripts of anaconda prompt to env variables of my account
  --in anaconda prompt, give 'where conda' to fetch paths


AWS Elastic Bean Stalk : Its a service provided by AWS to deploy and scale the web applications.Its instance is created in ebextensions\python.config file. It contains the entry point of the application ie., 'application' . Since we dont have any application.py till now, we make application.py with the code of app.py. This application.py is for deployment of the app in AWS.