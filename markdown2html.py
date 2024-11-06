#!/usr/bin/python3
"""A script to convert README to HTML"""
import sys

if (len(sys.argv) < 2):
    print('Usage: ./markdown2html.py README.md README.html')
    exit(1)

if (len(sys.argv) == 3):
    try:
        with open(sys.argv[1], encoding='utf-8') as f:
            pass
    except:
        print(f'Missing {sys.argv[1]}', file=sys.stderr)
        exit(1)
