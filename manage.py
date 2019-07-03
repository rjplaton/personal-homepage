import utils
import sys


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


def main():
    utils.auto_discover_content_files()
    utils.update_doc_htmls()
    

    #blog files still using older functions, will update
    i = 0
    for blog_post in blog_posts:
        utils.replace_blog_strings(blog_post)
        utils.replace_blog_content(blog_post)
        i +=1
    return print('- - - -',i,"out of", len(blog_posts), "blogs in /doc/ updated. - - - -")



print("This is argv:", sys.argv)
command = sys.argv[1]
print(command)
if command == "build":
    print("Build was specified")
    main()
elif command == "new":
    utils.new_file_creation()
    main()
else:
    print("Please specify ’build’ or ’new’ after python3 manage.py")
    print("e.g. manage.py build OR manage.py new")



# if __name__ == "__main__":
#     main()