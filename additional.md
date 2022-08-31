# Additional Info
Hello! This is out of the way, on purpose. Congratulations on finding it. It's not necessary, but may prove helpful?


## Custom commands
You can add custom commands to git. All you have to do is put an executable on your path named `git-<name>` and you'll be able to invoke it with `git <name>`--the hyphen is replaced by a space. Note that the executable can't have an extension on it--you may need to add a [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) and/or create a [symlink](https://en.wikipedia.org/wiki/Symbolic_link).

I've included the two I've written in the `git-commands` folder in this branch of the repo. `git-wherewasi` is a simple `bash` script; `git-new-branch` (invoked as `git new-branch <name>`) is a symlink to a python script.
