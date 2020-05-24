# Project name here
> Summary description here.


This file will become your README and also the index of your documentation.

## Install
1. Make a conda env with nbdev installed in it.
2. Activate that env and run nbdev `<project_name>`. This will create a git-initialized repo with `$PWD/<project_name>`.
3. Run `nbdev_install_git_hooks`.
4. Run `nbdev_build_lib`. This will create a Makefile on its first run.
5. `make docs_serve` – This will most likely fail on your first run, as it tries to use Jekyll locally similarily on how it will later look using github pages.
  1. Goto docs directory inside `<project_name>`.
  2. `bundle install --path ~/.local/<project_name>-docs` – This is only needed to serve the documentation locally! It pulls in a lot of ruby stuff.

## How to use

Fill me in please! Don't forget code examples:

```python
1+1
```




    2


