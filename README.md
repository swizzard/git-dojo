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
* `git branch -m <new-name>` will change the name of your current branch, _but only locally_. There are ways to fix a misnamed branch on a remote, but they're fussy, so it's better to get it right _before_ you push.


## Committing
To "save" your work with Git, you `commit` it. Committing is a two-step process, which can frustrate and confuse new users.
1. `add` work with `git add <path>`. This will result in the file(s) being "staged," or ready to be committed.
2. `commit` with `git commit`. _Everything_ that is staged--and _nothing_ that is not--will be part of the commit.
Before a commit is finalized, you have to write a 'commit message.' Commit messages are a Whole Thing, and likely merit their own Dojo, but briefly:
* Have a convention and stick to it.
* _Don't_ say what files are in the commit or what changes you made--that's available elsewhere.
* Similarly, _don't_ identify yourself--that's available elsewhere as well.
* _Do_ say what you did and (ideally) why.
Good commit messages share much in common with good comments.
NB: Github treats the first line of a commit message as a kind of header or title.

Every time you commit, it adds to the `history`. This is good, because it means there's a record of what's been done. If you make a mistake, you can always fix it and then make another commit. (There are [secret things](#secret-things) you can do about that, however.)


## Secret Things
* If you really want to make changes to a commit you've already made (but _have not [pushed](#pulling-and-pushing)_), you can use `git commit --amend` to re-open the commit editor. This will let you remove committed files (by commenting them out) or change the commit message. Bear in mind that `git commit --amend` only lets you edit your most recent commit.

