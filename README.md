# Git Dojo

## Initialize a new repo
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
Branches are like paths your work can take. When you [initialize a new repo](#initialize-a-new-repo), you start on the default branch (e.g. `main`). You can always `fork` off a new branch; your new branch will be identical to the branch from which it was forked. Anything you do in a branch won't affect any other branch. Once you're satisfied with your work, you can [`commit`](#committing) your work and [`merge`](#merging) it into another branch (e.g., the default branch.)
* `git switch -c <name>` will `c`reate a new branch off of the branch you're currently on.
  * Older Git references (and users) will use `git checkout -b <name>` instead. This is fine, but `git checkout` is extremely overloaded (i.e. does too many things.) `git switch` was added to handle some of `checkout`'s responsibilites and should generally be prefered.
* `git switch <name>` (without `-c`) will switch to a given branch. If the branch doesn't exist, you'll get an error.
* `git switch -` will switch you back to the previous branch you were on.
* `git branch -m <new-name>` will change the name of your current branch, _but only locally_. There are ways to fix a misnamed branch on a remote, but they're fussy, so it's better to get it right _before_ you push.
* `git checkout <branch> -- <path>` will change the state of `<path>` to what it is in `<branch>`--think of it like a very localized `git switch`. This works even if the path _doesn't exist_ in your current branch. Anything you `checkout` from another branch is `staged` but you still have to [`commit`](#committing) it.

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

If, for whatever reason, you want to bail without committing, you can delete or comment out (with `#`) everything in the commit message.

Every time you commit, it adds to the `history`. This is good, because it means there's a record of what's been done. If you make a mistake, you can always fix it and then make another commit.

If you really want to make changes to a commit you've already made (but _have not [pushed](#pulling-and-pushing)_), you can use `git commit --amend` to re-open the commit editor. This will let you remove committed files (by commenting them out) or change the commit message. Bear in mind that `git commit --amend` only lets you edit your most recent commit. If you delete or comment out everything while amending, it won't "undo" the commit--it'll just leave it as is.

## Merging
In order to get the work done in one branch into another branch, it needs to be `merged`. Most of the time, this should be done by opening a pull request on GitHub and having your peers review the code you want to merge. Not only does GitHub provide a nice-looking visual interface with affordances for comments, etc., it also makes it easy to `squash and merge`, which [`rebases`](#rebasing) all the commits in a branch into one single commit, and then merges that. Since the entire branch is represented in one commit, it's much easier to `rebase` out or revert. When you open a PR on GitHub, you might see a warning that your branch cannot be merged automatically. In that case, it's up to you to pull the latest changes to main into your branch and resolve any conflicts (see below.)
* `git merge <branch>` will merge the changes made in `<branch>` into your current branch. Git is generally pretty good about figuring how best to do this, and most of the time it should go smoothly. Sometimes, however, there will be `merge conflicts`. Git will let you know when this happens; it's up to you to resolve the conflicts. Git will add special formatting within the affected files to call attention to the conflicts. It looks like
```
<<<<<<<<<<<<<<<<<< HEAD: <filename>
<stuff as it is in HEAD>
==================
<stuff as it is in the commit you're merging>
>>>>>>>>>>>>>>>>> <commit id>: <filename>
```
Usually you'll pick one side (above or below the `====`) and delete the rest, but you're free to mix and match, or delete all of it and replace it with something else entirely. The important thing is that you delete the `<<<<<< ====== >>>>>>`, save the change, and then mark the conflict as `resolved` with `git add`. Once you've resolved all the conflicts, finalize the merge with `git merge --continue`. You can also bail with `git merge --abort` (just like when you're [`rebasing`](#rebasing) or [`cherry-picking`](#cherry-picking).)
* `git merge <branch> --theirs` works like regular merging, but precludes conflicts by deferring to what's in `<branch>`. Similarly, `git merge <branch> --ours` will use what's in your current branch over what's in the branch you're merging in.

## Rebasing other branches
Instead of merging branches, you can rebase them instead. Full disclosure: this is one of my biggest git blind spots. It's usually discussed in terms of "replaying commits" from one branch "on top" of another. I don't really know what that means. I'm familiar and comfortable with using `git rebase -i` to edit the history of a branch, but almost never rebase one branch into (onto?) another. I've tried it a few times; it's always been stressful and I've always regretted not just merging instead. That said, there's assuredly a reason for it, and situations in which it is absolutely called for instead of a regular merge.
