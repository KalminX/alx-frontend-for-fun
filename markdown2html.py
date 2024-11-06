#!/usr/bin/python3
"""A script to convert README to HTML"""
import sys


def main():
    if (len(sys.argv) < 2):
        print('Usage: ./markdown2html.py README.md README.html')
        exit(1)

    if (len(sys.argv) == 3):
        try:
            with open(sys.argv[1], encoding='utf-8') as f:
                lines = f.readlines()
                html_list = []
                for line in lines:
                    level = line.count('#')
                    line = list(line)
                    while ('#' in line):
                        line.remove('#')
                    line = ''.join(line).strip()
                    html_list.append(f"<h{level}>{line}</h{level}>\n")
                with open(sys.argv[2], 'w', encoding='utf-8') as file:
                    file.writelines(html_list)
                        
        except FileNotFoundError:
            print(f'Missing {sys.argv[1]}', file=sys.stderr)
            exit(1)


if __name__ == "__main__":
    main()
