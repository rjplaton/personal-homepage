from string import Template

template_text = open('./templates/template.html').read()
template = Template(template_text)

#list of every page and the strings to replace
pages = [ {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Personal Projects & More",
        "meta_description": "Welcome to Reuben's personal project site",
        "index_class": 'class="current-item"',
}, 
{
        "filename": "content/blog.html",
        "output": "docs/blog.html",
        "title": "Blog",
        "meta_description": "Blogging about stuff",
        "blog_class": 'class="current-item"',
}, 
{
        "filename": "content/contact.html",
        "output": "docs/contact.html",
        "title": "Contact Me",
        "meta_description": "Contact me through the contact form on this page",
        "contact_class": 'class="current-item"',
},
{
        "filename": "content/projects.html",
        "output": "docs/projects.html",
        "title": "Projects & More",
        "meta_description": "Current & Past Coding Projects",
        "projects_class": 'class="current-item"',
},
]

#function to replace template values
def replace_template_values():
    for page in pages:
        print(page['filename'])
        full_page = template.safe_substitute(page)
        open(page['output'], 'w+').write(full_page)

        #replace the content section with /content/ pages
        content = open(page['filename']).read()
        full_page = full_page.replace("{content}", content)
        open(page['output'], 'w+').write(full_page)
        print('Completed: ',page['output'])

replace_template_values()