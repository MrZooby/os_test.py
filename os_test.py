#!/usr/bin/env python3

import os
import sys
import argparse

def get_files(path):
    return os.listdir(path)

def read_file(file):
    file = open(file)
    return file

parser = argparse.ArgumentParser()
parser.add_argument("-p","--path", help="Enter directory to read")
parser.add_argument("-f","--file", help="Full path of file to read")
parser.add_argument("-s","--search", help="search given file")
args = parser.parse_args()
if len(sys.argv) == 1:
    parser.print_help()
if args.path:
    list = get_files(args.path)
    for word in list:
        print(word)
if args.file:
    file = read_file(args.file)
    print(file.read())
if args.search:
    if args.file is None:
        raise Exception("-f required when using this option")
    line_count = 0
    file = read_file(args.file)
    for line in file:
        if args.search in line:
            line_count += 1
            print(line, end='')
    print(f"\n There are {line_count} matches")