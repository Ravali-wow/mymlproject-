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