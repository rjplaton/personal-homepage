from string import Template
#some_string = 'Hi ${name}, how are you?'
#template = Template(some_string)
#print(template.safe_substitute(name='Ash Ketchum'))

template_text = open('./templates/template.html').read()
template = Template(template_text)

#build the index.html page using template.html
index_content = open('./content/index.html').read()
index_page = template.safe_substitute(
    title="Personal Projects & More",
    index_class="current-item",
    content=index_content,
    meta_description="Welcome to Reuben's personal project site"
)
open('./docs/index.html', 'w+').write(index_page)

#repeating above for blog, projects, contact

blog_content = open('./content/blog.html').read()
blog_page = template.safe_substitute(
    title="Blog",
    blog_class="current-item",
    content=blog_content,
    meta_description="Blogging about stuff"
)
open('./docs/blog.html', 'w+').write(blog_page)


projects_content = open('./content/projects.html').read()
projects_page = template.safe_substitute(
    title="Projects",
    projects_class="current-item",
    content=projects_content,
    meta_description="Current and past coding projects and more"
)
open('./docs/projects.html', 'w+').write(projects_page)


contact_content = open('./content/contact.html').read()
contact_page = template.safe_substitute(
    title="Contact Me",
    contact_class="current-item",
    content=contact_content,
    meta_description="Contact me through the contact form on this page"
)
open('./docs/contact.html', 'w+').write(contact_page)
