from multiprocessing.sharedctypes import Value
import subprocess
from sys import stderr

upper = '''
<!DOCTYPE HTML>
<html>
    <head>
        <title>zifmann.tech::Blogs</title>
        <style>
            html, body {
                margin: 0;
                padding: 0;
                background-color: #1d2123;
                color: white;
            }
            header {
                background-color: white;
                padding: 20pt 50pt;
                font-size: 20pt;
                font-family: 'IBM Plex Sans', sans-serif;
                color: black;
            }
            header span {
                font-weight: lighter;
            }
            #parent-content {
                padding: 20pt 50pt;
            } 
            date::before {
                content: "Date:";
            }
            date {
                font-family: sans-serif;
                font-size: 12px;
                display: block;
            }
        </style>
    </head>
    <body>
        <div class="container" id="main">
            <header>
                zifmann.tech<span>::Blogs</span>
            </header>
            <div id="parent-content">
                <section id="featured-banner">
'''
mid = '''
                </section>
            </div>
'''

end = '''
        </div>
    </body>
</html>
'''

class BlogPost(object):

    def __init__(self, date, content, title, author, brief):
        self.date = date
        self.content = content
        self.title = title
        self.author = author
        self.brief = brief


def format_date(date):
    date_formatted = []
    builder = ""
    for c in date:
        if c in ' \t-\n':
            if builder:
                try:
                    date_formatted.append(int(builder))
                    builder = ""
                except ValueError as error:
                    print(error)
                    return None
    return date_formatted


def generate_homepage(blog):
    global upper, mid, end
    html = upper
    html += '<article>\n<title>' + blog.title + '</title>\n'
    html += '<date>' + blog.date + '</date>\n'
    html += '<author>' + blog.author + '</author>\n'
    html += '<content>\n' + blog.brief + '\n</content>\n'
    html += mid
    html += end
    with open('homepage.html', 'w') as homepage_file:
        homepage_file.write(html)


def add_blog_post(path):
    post = None
    with open(path, 'r') as blog_file:
        date = blog_file.readline()
        title = blog_file.readline()
        author = blog_file.readline()
        brief = blog_file.readline()
        content = blog_file.read()
        post = BlogPost(date, content, title, author, brief)
    if post:
        generate_homepage(post)
    else:
        print('Lol no blog found!')


add_blog_post('blog.txt')