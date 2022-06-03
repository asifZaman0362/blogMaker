class BlogPost(object):

    def __init__(self, title, author, categories, date, content):
        self.title = title
        self.author = author
        self.categories = categories
        self.date = date
        self.content = content

    def generate_html_main_post(self):
        newline = '\n                        '
        html = f'''
        <article>
            <section class="meta">
                <h1 class="title">{self.title}</h1>
                <date>{self.date}</date>
                <author>{self.author}</author>
                <categories>
                    <ul>
                        {newline.join(['<li>' + category + '</li>' for category in self.categories])}
                    </ul>
                </categories>
            </section>
            <p class="content">{self.content}</p>
        </article>
        '''
        return html

    def generate_html_summary(self):
        html = f'''
        <article>
            <h1 class="title">{self.title}</h1>
            <date>{self.date}</date>
            <author>{self.author}</author>
            <p class="content">{self.content}</p>
        </article>
        '''
        return html

class BlogPostParser(object):

    def __init__(self, filename):
        self.filename = filename
    
    def parse_blog_post(self) -> BlogPost:
        with open(self.filename, 'r') as file:
            title = file.readline().replace('\n', '')
            author = file.readline().replace('\n', '')
            date = file.readline().replace('\n', '')
            categories = file.readline().replace('\n', '').split(';')
            content = file.read()
        return BlogPost(title, author, categories, date, content)
