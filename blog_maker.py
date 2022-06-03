#!/bin/python

import argparse

from blogpost import BlogPostParser
from html_writer import write_post_html, generate_homepage

def get_files(filenamelist):
    files = filenamelist.split(',')
    return files if len(files) else None

def add_post(filename):
    with open('data/posts.db', 'w') as database:
        names = database.read().split('\n')
        if filename in names:
                return False
        if len(names) > 10:
            names.pop()
        names = [filename] + names
    # generate html for main blog page
    blogpost = BlogPostParser(filename).parse_blog_post()
    blog_post_html = blogpost.generate_html_main_post()
    summary_html = blogpost.generate_html_summary()
    # generate html summaries for the last eleven entries
    summaries = []
    with open('data/posts.db', 'w') as database:
        names = database.read().split('\n')
        for post in names:
            if post == filename:
                continue
            # generate summary html
            blogpost = BlogPostParser(post).parse_blog_post()
            summaries.append(blogpost.generate_html_summary())
            # write summary html into homepage
    generate_homepage(summaries=summaries, featured=summary_html)
    write_post_html(blogpost, blog_post_html)

def main():
    arg_parser = argparse.ArgumentParser(description="A minimal static blog generator")
    arg_parser.add_argument("mode", help="Available modes: add, update and remove")
    arg_parser.add_argument("filenamelist", help="List of .blog files seperated by commas and no spaces")
    args = arg_parser.parse_args()

    files = get_files(args.filenamelist)
    if files:
        match args.mode:
            case "add":
                for f in files:
                    # with open(f, 'r'):
                    #     # TODO: Add blog post
                    #     pass
                    print(f'Adding {f}...')
            case "update":
                for f in files:
                    # with open(f, 'r'):
                    #     # TODO: Update blog post
                    #     pass
                    print(f'Updating {f}...')
            case "remove":
                for f in files:
                    # with open(f, 'r'):
                    #     # TODO: Remove blog post
                    #     pass
                    print(f'Removing {f}...')
            case _:
                print("Not a valid mode. Expected one of [-u, -a, -r]")

if __name__ == "__main__":
    main()