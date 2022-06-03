import pathlib

top = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>zifmann.tech::blog</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <div id="textmark">
            <a href="https://zifmann.tech">zifmann<span id="domainextension">tech<span id="subdomain">blog</span></span></a>
        </div>
        <nav>
            <ul>
                <li><a href="/blog.html">blog</a></li>
                <li><a href="/store.html">store</a></li>
                <li><a href="/github.html">github</a></li>
                <li><a href="/projects.html">projects</a></li>
                <li><a href="/about.html">about</a></li>
            </ul>
        </nav>
    </header>
    <div id="parent">
        <div id="grid">
            <div id="posts-overview">
'''
featured_start = '''
                <section id="featured">
'''
featured_end = '''
                </section>
'''
overview_start = '''
                <section id="overview">
'''
overview_end = '''
                </section>
'''
end = '''
            </div>
            <div id="sidebar">
                <nav>
                    <h2>Categories</h2>
                    <ul>
                        <li><a href="/blog/category.html">Catergory name</a></li>
                        <li><a href="/blog/category.html">Catergory name</a></li>
                        <li><a href="/blog/category.html">Catergory name</a></li>
                        <li><a href="/blog/category.html">Catergory name</a></li>
                        <li><a href="/blog/category.html">Catergory name</a></li>
                        <li><a href="/blog/category.html">Catergory name</a></li>
                    </ul>
                </nav>
                <nav>
                    <h2>Archives</h2>
                    <ul>
                        <li><a href="/blog/archives/jan.html">January 2022</a></li>
                        <li><a href="/blog/archives/jan.html">January 2022</a></li>
                        <li><a href="/blog/archives/jan.html">January 2022</a></li>
                        <li><a href="/blog/archives/jan.html">January 2022</a></li>
                        <li><a href="/blog/archives/jan.html">January 2022</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </div>
</body>
</html>
'''

blogpost_header = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>zifmann.tech::blog::post</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <div id="textmark">
            <a href="https://zifmann.tech">zifmann<span id="domainextension">tech<span id="subdomain">blog</span></span></a>
        </div>
        <nav>
            <ul>
                <li><a href="/blog.html">blog</a></li>
                <li><a href="/store.html">store</a></li>
                <li><a href="/github.html">github</a></li>
                <li><a href="/projects.html">projects</a></li>
                <li><a href="/about.html">about</a></li>
            </ul>
        </nav>
    </header>
    <div id="post-parent">
        <div id="post-container">
'''

blogpost_footer = '''
        </div>
    </div>
</body>
</html>
'''

def generate_homepage(summaries, featured):
    try:
        with open('index.html', 'w') as homepage:
            homepage.write(top)
            homepage.write(featured_start)
            homepage.write(featured)
            homepage.write(featured_end)
            for summary in summaries:
                homepage.write('<a class="post-excerpt" href="post.html">')
                homepage.write(summary)
                homepage.write('</a>')
            homepage.write(end)
            return True
    except IOError as error:
        print(error)
        return False

def write_post_html(post, html):
    try:
        filepath = pathlib.Path('data').joinpath(post.title + '.html')
        with open(filepath, 'w') as file:
            file.write(blogpost_header)
            file.write(html)
            file.write(blogpost_footer)
            return True
    except IOError as error:
        print(error)
        return False
