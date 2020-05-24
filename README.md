# Sully
> Exploratory Data Analysis (EDA) on bird strikes in aviation.


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

## How to use

Each notebook is transpiled to one web page. Code cells that are marked with `#export` become part of your project's library (or module). This enables you to A) reuse code in other notebooks, B) run your analysis from CLI, without Jupyter.

The first markdown cell of each notebook is treated special by nbdev; it contains the (only) first level headline followed by a brief section describing the notebooks contents like so:

~~~
# Awesome Notebook Does Amazing Things Only Ever Done A Million Times Before

> This is an exec summary of your notebook. Keep it brief and to the point.
~~~

If you care about a proper project website, you'll need to do this for each of your project's notebooks! The first level headline of each notebook is used to create the sidebar menu. Proper headline structuring and nesting is recommended once the headlines pile up, as the `make docs` functionality will automagically create a TOC for your notebook. 
