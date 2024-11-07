#!/usr/bin/python3
"""A script to convert README to HTML"""
import sys


def main():
    """The entry point of my script"""
    if (len(sys.argv) < 3):
        print('Usage: ./markdown2html.py README.md README.html', file=sys.stderr)
        exit(1)

    if (len(sys.argv) == 3):
        try:
            with open(sys.argv[1], encoding='utf-8') as f:
                lines = f.readlines()
                special_ch = ['#', '-', '*']
                html_list = []
                for index, line in enumerate(lines):
                    if line.strip().startswith('#'):
                        md_heading_2_html(line, html_list)
                    elif line.strip().startswith('-'):
                        md_ul_list_2_html(index, line, lines, html_list)
                    elif line.strip().startswith('*'):
                        md_ol_list_2_html(index, line, lines, html_list)
                    elif line == '\n':
                        html_list.append('<br/>\n')
                    else:
                        md_text_2_html(index, line, lines, html_list)

                with open(sys.argv[2], 'w', encoding='utf-8') as file:
                    file.writelines(html_list)

        except FileNotFoundError:
            print(f'Missing {sys.argv[1]}', file=sys.stderr)
            exit(1)


def md_text_2_html(index, line, lines, html_list):
    pass


def md_heading_2_html(line, html_list):
    """A function that handles conversion of markdown heading"""
    level = line.count('#')
    line = list(line)
    while ('#' in line):
        line.remove('#')
    line = ''.join(line).strip()
    html_list.append(f"<h{level}>{line}</h{level}>\n")


def md_ul_list_2_html(index, line, lines, html_list):
    """A function that handles conversion of markdown unordered list"""
    if index == 0:
        html_list.append('<ul>\n')
    else:
        try:
            if (not lines[index - 1].startswith('-')):
                html_list.append('<ul>\n')
        except:
            pass
    try:
        if (lines[index + 1].startswith('-')):
            html_list.append(f'<li>{line[2:-1]}</li>\n')
        else:
            html_list.append('</ul>\n')
    except IndexError:
        html_list.append(f'<li>{line[2:]}</li>\n')
        html_list.append('</ul>\n')
    except:
        pass


def md_ol_list_2_html(index, line, lines, html_list):
    """A function that handles conversion of markdown unordered list"""
    if index == 0:
        html_list.append('<ol>\n')
    else:
        try:
            if (not lines[index - 1].startswith('*')):
                html_list.append('<ol>\n')
        except:
            pass
    try:
        if (lines[index + 1].startswith('*')):
            html_list.append(f'<li>{line[2:-1]}</li>\n')
        else:
            html_list.append('</ol>\n')
    except IndexError:
        html_list.append(f'<li>{line[2:]}</li>\n')
        html_list.append('</ol>\n')
    except:
        pass


if __name__ == "__main__":
    main()
