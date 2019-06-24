# Personal Homepage Project
# [![rjplaton](http://rjplaton.com/img/core-img/logo.png)](http://rjplaton.com)
Powering my personal site at [rjplaton.com](http://rjplaton.com) featuring my profile, projects & blog. It's a playgound for building and iterating on a concepts and things I've learned in programming.


### Current tech stack:
- HTML
- CSS
- Bootstrap
- Python

Python is being used to automate the generation of the site by combining content pages with a template.

### Instructions on updating the website:
1. To update body content of specific pages, update the pages in /content/: 
2. To update page specific values like `title` &  `meta-description`, update the `pages` dict contained in `build.py`
3. To update the common header and footer, update template.html in /templates/
4. Run build.py to automtically apply changes to all user facing "full pages" in /docs/
```sh
$ python3 build.py
```
