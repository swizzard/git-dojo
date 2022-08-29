# Git Dojo

## Initialize a new repo
A `repository` (or `repo`) is 
* `git init`
  * if you have `>= 2.28` (`git --version` to check) you can change the default branch name
    * pass `-b main`/`--initial-branch=main` to initialize the new repo with `main` as the default branch
    * use [`git config`](#configuring-git) `--global init.defaultBranch main`

## Remotes
Remotes are places where your code lives. Most of the time, this will be on github, but it _doesn't have to be_. Other options include [gitlab](https://about.gitlab.com/); you can even host your own git server.
* `git remote -v` will show you a list of remotes
* `git remote add <name> <url>` will add a remote
  * `name` is how you identify the remote to git, when you e.g. [`pull`](#pulling-and-pushing) or [`push`](#pulling-and-pushing)
* `git remote set-url <name> <url>` will update the url of a remote by name
* `git remote remove <name>` will remove a repo by name

## Branches
Branches are like paths your work can take. When you [initialize a new repo](#initialize-a-new-repo), you start on the default branch (e.g. `main`). You can always `fork` off a new branch; your new branch will be identical to the branch from which it was forked. Anything you do in a branch won't affect any other branch. Once you're satisfied with your work, you can [`merge`](#merging) your work into another branch (e.g., the default branch.)
* `git switch -c <name>` will `c`reate a new branch off of the branch you're currently on.
  * Older Git references (and users) will use `git checkout -b <name>` instead. This is fine, but `git checkout` is extremely overloaded (i.e. does too many things.) `git switch` was added to handle some of `checkout`'s responsibilites and should generally be prefered.
* `git switch <name>` (without `-c`) will switch to a given branch. If the branch doesn't exist, you'll get an error.
* `git switch -` will switch you back to the previous branch you were on.
