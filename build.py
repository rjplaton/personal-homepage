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

def replace_template_strings(page):
    """replace strings in template"""
    #using Template strings and safesubstitute to replace values
    #moved the import into this function as it is only used by this function
    from string import Template
    template_text = open('./templates/template.html').read()
    template = Template(template_text)
    print('Updating:', page['filename'])
    updated_page = template.safe_substitute(page)
    #writing the updates to the/doc/pages
    open(page['output'], 'w+').write(updated_page)

def replace_content_section(page):
    """replace the content section with /content/ pages"""
    content = open(page['filename']).read()
    doc_page = open(page['output']).read()
    #replacing and writing the doc pages with content
    full_page = doc_page.replace("{content}", content)
    open(page['output'], 'w+').write(full_page)
    return print('Completed: ',page['output'])


#list every blog post

blog_posts = [ {
        "filename": "content/blog/1.html",
        "date": "03 June 2019",
        "title": "Officially a student at Kickstart Coding",
        "output": "docs/blog/1.html"
},
{
        "filename": "content/blog/2.html",
        "date": "13 June 2019",
        "title": "Lorem ipsum 2",
        "output": "docs/blog/2.html"
},
{
        "filename": "content/blog/3.html",
        "date": "23 June 2019",
        "title": "Lorem ipsum dolor sit 3",
        "output": "docs/blog/3.html"
},
]

def replace_blog_strings(blog_post):
    from string import Template
    template_text = open('./templates/blog_base.html').read()
    template = Template(template_text)
    print('Updating:', blog_post['filename'])
    updated_page = template.safe_substitute(blog_post)
    open(blog_post['output'], 'w+').write(updated_page)

def replace_blog_content(blog_post):
    content = open(blog_post['filename']).read()
    post_page = open(blog_post['output']).read()
    full_page = post_page.replace("{content}", content)
    open(blog_post['output'], 'w+').write(full_page)
    return print('Completed: ',blog_post['output'])


def main():
    i = 0
    for page in pages:
        replace_template_strings(page)
        replace_content_section(page)
        i += 1
    #using i to count how many times the function looped 
    #and comparing with total number of list items
    print('- - - -',i,"out of", len(pages), "html pages in /doc/ updated. - - - -")
    i = 0
    for blog_post in blog_posts:
        replace_blog_strings(blog_post)
        replace_blog_content(blog_post)
        i +=1
    return print('- - - -',i,"out of", len(blog_posts), "blogs in /doc/ updated. - - - -")


if __name__ == "__main__":
    main()