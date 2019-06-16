#Define template
top = open('./templates/top.html').read()
bottom = open('./templates/bottom.html').read()

#Define content for index page
content = open('./content/index.html').read()

#Define combined page
index_page = top + content + bottom

#Build combined pages into /docs
open('./docs/index.html', 'w+').write(index_page)

#Test if it works for the index page
print('Successfully built the index.html page')

#Repeat above for blog, projects & contact
content = open('./content/blog.html').read()
blog_page = top + content + bottom
open('./docs/blog.html', 'w+').write(blog_page)
print('Successfully built the blog.html page')

content = open('./content/projects.html').read()
projects_page = top + content + bottom
open('./docs/projects.html', 'w+').write(projects_page)
print('Successfully built the projects.html page')

content = open('./content/contact.html').read()
contact_page = top + content + bottom
open('./docs/contact.html', 'w+').write(contact_page)
print('Successfully built the contact.html page')