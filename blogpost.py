import markdown

class BlogPost(object):

    def __init__(self, title, author, categories, date, content):
        self.title = title
        self.author = author
        self.categories = categories
        self.date = date
        self.content = markdown.markdown(content)

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
            line = file.readline().replace('\n', '')
            if line == '$meta':
                line = file.readline().replace('\n', '')
                while line:
                    if line == '$endmeta':
                        break
                    else:
                        tokens = line.split(':')
                        match tokens[0]:
                            case 'author':
                                author = tokens[1]
                            case 'date':
                                date = tokens[1]
                            case 'categories':
                                categories = tokens[1].split(',')
                            case 'title':
                                title = tokens[1]
                            case _:
                                raise ValueError('Invalid token inside meta block : ' + tokens[0])
                    line = file.readline().replace('\n', '')
                content = file.read()
        if title and author and categories and date and content:
            return BlogPost(title, author, categories, date, content)
        else:
            raise ValueError('Failed to parse blog post. Not all metadata provided!')
