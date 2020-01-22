#!/usr/bin/env python3
# encoding: UTF-8

"""
    Take an integer n and a list of filenames. Append "n+i " to filenames where i increments for each file.
    Example:
        Input: 4 docs.txt lists.txt program.c
        Output: "4 docs.txt", "5 lists.txt", "6 program.c"
"""

import sys, os

def main():
    usage = """Usage: \n append_order.py starting_number filename1 filename2 filename3..."""
    if len(sys.argv) < 3:
        print(usage)
        return
    try:
        order = int(sys.argv[1])
    except ValueError:
        print(usage)
        return

    print('Parsing...')
    for filename in sys.argv[2:]:
        old_path = os.path.abspath(filename)
        last_slash = old_path.rindex('/')
        new_path = f'{old_path[:last_slash]}/{order} {old_path[(last_slash+1):]}'
        try:
            os.rename(old_path, new_path)
            order += 1
        except FileNotFoundError:
            print(f'Can\'t find file {filename}, skipped.')
    print('Done parsing.')

if __name__ == '__main__':
    main()
