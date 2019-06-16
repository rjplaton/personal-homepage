#Define template
top = open('./templates/top.html').read()
bottom = open('./templates/bottom.html').read()

#Define content
index = open('./content/index.html').read()
blog = open('./content/blog.html').read()
projects = open('./content/projects.html').read()
contact = open('./content/contact.html').read()

#Define combined pages
index_page = top + index + bottom
blog_page = top + blog + bottom
projects_page = top + projects + bottom
contact_page = top + contact + bottom

#Build combined pages into /docs
open('./docs/index.html', 'w+').write(index_page)
open('./docs/blog.html', 'w+').write(blog_page)
open('./docs/projects.html', 'w+').write(projects_page)
open('./docs/contact.html', 'w+').write(contact_page)
