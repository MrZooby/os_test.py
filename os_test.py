#!/usr/bin/env python3

import os
import sys
import argparse

def open_file(file):
    file = open(file)
    return file

parser = argparse.ArgumentParser()
parser.add_argument("-p","--path", help="Enter directory to list.")
parser.add_argument("-f","--file", help="Full path of file to read.")
parser.add_argument("-s","--search", help="Search file for instances of a given string.")
args = parser.parse_args()
if len(sys.argv) == 1:
    print(f"Python Version {sys.version}")
    parser.print_help()
if args.path:
    list = os.listdir(args.path)
    for word in list:
        print(word)
if args.file:
    if args.search is None:
        file = open_file(args.file)
        print(file.read())
    else:
        pass
if args.search:
    if args.file is None:
        raise Exception("-f required when using this option")
    line_count = 0
    file = open_file(args.file)
    for line in file:
        if args.search in line:
            line_count += 1
            print(line, end='')
    print(f"\n#######################\n\nThere are {line_count} matches!\n")