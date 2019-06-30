#list of pages and the strings to replace, empty and will be filled by the auto_disocver_content_files function
pages = []

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
        generic_meta_desc = name_only.capitalize() + " page on Reuben Platon's personal website"
        #add the information for each new file in the pages list    
        pages.append({
        #set to find html files in /content/    
        "filename": content,
        "title": name_only,
        #set to corresponding /docs/ output html
        "output": output,
        "meta_description": generic_meta_desc,
        'name_only': name_only,
        })
        i += 1
        #using i to count how many times the function looped 
        #and comparing with total number of list items
        print('- - - -',i,"out of", len(all_content_files), "files in /content/ processed. - - - -")

### USING JINJA2 Templating ###



def update_doc_htmls():
    """update all pages in the pages list to update template strings and write updated files to /docs/"""
    from jinja2 import Template
    i = 0
    for page in pages:
        content_page = open(page['filename']).read()
        template_html = open("./templates/base.html").read()
        template = Template(template_html)
        #using positional arugment
        output = template.render(
            pages=pages,
            title=page['title'],
            content=content_page,
            meta_description=page['meta_description'],
            )
        
        #using dict argument to include the nav_class variable
        # output = template.render(
        #      {
        #      'title': page['title'],
        #      'content': content_page,
        #      'meta_description': page['meta_description'],
        #      nav_class: page[nav_class],
        #      }
        #      )
        open(page['output'], 'w+').write(output)
        i += 1
        print('- - - -',i,"out of", len(pages), "html files in /docs/ processed. - - - -")


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

 #blog files still using older functions, will update
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


def new_file_creation():
    print("New page was specified")
    new_page_title = input('What should the title of the new page be?   ')
    ### for new page content, consider extending the base template using the Contact page as a template
    open('content/' + new_page_title + '.html', 'w+').write("""
  <div class="breadcumb-area">
    <div class="container h-100">
      <div class="row h-100 align-items-end">
        <div class="col-12">
          <div class="breadcumb--con">
            <h2 class="title">""" + str(new_page_title) + """</h2>
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="./index.html"><i class="fa fa-home"></i> Home</a></li>
                <li class="breadcrumb-item active" aria-current="page">""" + str(new_page_title) + """</li>
              </ol>
            </nav>
          </div>
        </div>
      </div>
    </div>
  </div>
        """)











