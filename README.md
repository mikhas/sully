# Sully
> Exploratory Data Analysis (EDA) on <a href='https://en.wikipedia.org/wiki/US_Airways_Flight_1549'>bird strikes in aviation](https://www.kaggle.com/breana/bird-strikes). The project's name is a reference to the [Miracle on the Hudson on January 15, 2009</a>.


## Install
1. Make a conda env [with nbdev installed](https://nbdev.fast.ai/) in it.
2. Activate that env and run `nbdev_new <project_name>`. This will create a git-initialized repo with `$PWD/<project_name>`.
3. Run `nbdev_install_git_hooks`.
4. Run `nbdev_build_lib`. This will create a Makefile on its first run.
5. Modify `settings.ini` to reflect your github setup. You also specify your project's dependencies here for the github CI pipeline. 
6. `make docs_serve` – This will most likely fail on your first run, as it tries to use Jekyll locally similarily on how it will later look using github pages.
  1. Goto docs directory inside `<project_name>`.
  2. `bundle install --path ~/.local/<project_name>-docs` – This is only needed to serve the documentation locally! It pulls in a lot of ruby stuff.
7. Save your notebooks and **run `make all` before each `git {add, commit}`** – this might feel strange but the artifacts created by `make` are part of your project's git repository. This is intentional!
8. Push to github to check that CI runs successfully! Fix any build failures in this early stage before adding new stuff. Simulating github CI locally is possible but requires docker and an ungodly amount of npm stuff (read: security nightmare).
9. After your first push to github configure the github settings for your repository to enable github pages; point them to `branch: master, directory: docs/`. It can take up to 15min to build your github pages initially.
10. Goto `https://<github_username>.github.io/<project_name>/`. If you installed/configured everything correctly this should show your project's `index.ipynb` as landing page.
