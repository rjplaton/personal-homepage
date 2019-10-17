# Personal Homepage Project
# [![rjplaton](http://rjplaton.com/img/core-img/logo.png)](http://rjplaton.com)
Powering my personal site at [rjplaton.com](http://rjplaton.com) featuring my profile, projects & blog. It's a playgound for building and iterating on a concepts and things I've learned in programming.


### Current tech stack:
- HTML
- CSS
- Bootstrap
- Python
- Jinja2

Python is being used to automate the generation of the site by combining content pages with a template.

### Instructions on updating the website:
1. To update body content of specific pages, update the pages in /content/: 
2. To update the common header and footer, update base.html in /templates/
3. `pipenv shell`
4. Ensure Jinja2 is installed `pip install Jinja2`
5. Run `manage.py build` to automtically apply changes to all user facing "full pages" in /docs/
6. You can also create new pages with `manage.py new`. This will ask you for a page title and create a file within /content/ that will be built and rendered as a full page in /docs/

```sh
$ python3 manage.py build
```
