from string import Template
#some_string = 'Hi ${name}, how are you?'
#template = Template(some_string)
#print(template.safe_substitute(name='Ash Ketchum'))

template_text = open('./templates/template.html').read()
template = Template(template_text)

#build the index.html page using template.html
index_content = open('./content/index.html').read()
index_page = template.safe_substitute(
    title="Reuben J. Platon",
    index_class="current-item",
    content=index_content,
)
open('./docs/index.html', 'w+').write(index_page)