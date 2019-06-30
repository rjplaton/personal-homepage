#list of key pages and the strings to replace
pages = [ {
        "filename": "content/index.html",
        "output": "docs/index.html",
        "title": "Personal Projects & More",
        "meta_description": "Welcome to Reuben's personal project site",
        "index_class": 'class="current-item"',
        "name_only": 'index',
}, 
{
        "filename": "content/blog.html",
        "output": "docs/blog.html",
        "title": "Blog",
        "meta_description": "Blogging about stuff",
        "blog_class": 'class="current-item"',
        "name_only": 'blog',
}, 
{
        "filename": "content/contact.html",
        "output": "docs/contact.html",
        "title": "Contact Me",
        "meta_description": "Contact me through the contact form on this page",
        "contact_class": 'class="current-item"',
        "name_only": 'contact',
},
{
        "filename": "content/projects.html",
        "output": "docs/projects.html",
        "title": "Projects & More",
        "meta_description": "Current & Past Coding Projects",
        "projects_class": 'class="current-item"',
        "name_only": 'projects',
},
]

#auto generate pages it finds in the /content/ directory
def auto_discover_content_files():
    """find pages in the /content/ directory & append info to the pages list"""
    import glob
    import os
    all_content_files = glob.glob("content/*.html")
    i = 0
    for content in all_content_files:
        file_path = content
        file_name = os.path.basename(file_path)
        #will print blog.html
        print('Working on:',file_name)
        name_only, extension = os.path.splitext(file_name)
        #will print blog
        output = "docs/" + file_name
        nav_class = name_only + "_class"
        generic_meta_desc = name_only.capitalize() + " page on Reuben Platon's personal website"
        #add the information for each new file in the pages list    
        pages.append({
        #set to find html files in /content/    
        "filename": content,
        "title": name_only,
        #set to corresponding /docs/ output html
        "output": output,
        "meta_description": generic_meta_desc,
        #set nav_class used for setting active class
        nav_class: 'class="current-item"',
        'name_only': name_only,
        })
        i += 1
        #using i to count how many times the function looped 
        #and comparing with total number of list items
        print('- - - -',i,"out of", len(all_content_files), "html files in /content/ processed. - - - -")

### USING JINJA2 Templating ###

def update_doc_htmls():
    """update all pages in the pages list to update template strings and write updated files to /docs/"""
    from jinja2 import Template
    for page in pages:
        content_page = open(page['filename']).read()
        template_html = open("./templates/base.html").read()
        template = Template(template_html)
        #defining nav_class as it is dynamically generated per page
        nav_class = page['name_only'] + '_class'
        #using dict argument to include the nav_class variable
        output = template.render(
             {
             'title': page['title'],
             'content': content_page,
             'meta_description': page['meta_description'],
             nav_class: page[nav_class],
             }
             )
        open(page['output'], 'w+').write(output)


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
    auto_discover_content_files()
    update_doc_htmls()
    i = 0
    for blog_post in blog_posts:
        replace_blog_strings(blog_post)
        replace_blog_content(blog_post)
        i +=1
    return print('- - - -',i,"out of", len(blog_posts), "blogs in /doc/ updated. - - - -")


if __name__ == "__main__":
    main()