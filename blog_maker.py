#!/bin/python

import os, subprocess
import argparse

def get_files(filenamelist):
    files = filenamelist.split(',')
    return files if len(files) else None

def main():
    arg_parser = argparse.ArgumentParser(description="A minimal static blog generator")
    arg_parser.add_argument("mode", help="Available modes: -a (add), -u (update) and -r  (remove)")
    arg_parser.add_argument("filenamelist", help="List of .blog files seperated by commas and no spaces")
    args = arg_parser.parse_args()

    files = get_files(args.filenamelist)
    if files:
        match args.mode:
            case "-a":
                for f in files:
                    with open(f, 'r'):
                        # TODO: Add blog post
                        pass
            case "-u":
                for f in files:
                    with open(f, 'r'):
                        # TODO: Update blog post
                        pass
            case "-r":
                for f in files:
                    with open(f, 'r'):
                        # TODO: Remove blog post
                        pass
            case _:
                print("Not a valid mode. Expected one of [-u, -a, -r]")

if __name__ == "__main__":
    main()

# usage:
# zlog [mode] [filenamelist]
# zlog -a [filename,filename,...]
# zlog -u [filename,filename,...]
# zlog -r [filename,filename,...]
