#! /usr/bin/env python3

import os
import re
from subprocess import run
from sys import argv, exit


def branches_list():
    return run(
        ["git", "--no-pager", "branch", "--list"], capture_output=True, text=True
    ).stdout


def next_branch(branch_name):
    p = f"{branch_name}(?:-(\\w))?"
    matches = re.findall(p, branches_list())
    if len(matches) == 0:
        return branch_name
    matches.sort()
    m = matches[-1]
    if m == "":
        return f"{branch_name}-b"
    return f"{branch_name}-{chr(ord(matches[-1]) + 1)}"


def main():
    main_branch = os.getenv("GIT_MAIN_BRANCH", "main")
    if len(argv) != 2:
        print("Please supply a branch name")
        exit(1)
    branch_name = argv[1]
    run(["git", "switch", main_branch])
    run(["git", "pull", "origin", main_branch])
    run(["git", "switch", "-c", next_branch(branch_name)])
    exit(0)


if __name__ == "__main__":
    main()
