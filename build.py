#Define template
top = open('./templates/top.html').read()
bottom = open('./templates/bottom.html').read()

#Define content
content = open('./content/index.html').read()

#Define combined page
index_page = top + content + bottom

#Build combined pages into /docs
open('./docs/index.html', 'w+').write(index_page)

#Test if it works for the index page
print('Successfully built the index.html page')