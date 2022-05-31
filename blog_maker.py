#!/bin/python

import os, subprocess
import argparse

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("filename")
    args = arg_parser.parse_args()

    if args.filename:
        print(args.filename)

if __name__ == "__main__":
    main()
