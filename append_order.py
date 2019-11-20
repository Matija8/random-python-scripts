#!/usr/bin/env python3
# encoding: UTF-8

"""
    Take an integer n and a list of filenames. Append "n+i " to filenames where i increments for each file.
    Example:
        Input: 4 docs.txt lists.txt program.c
        Output: "4 docs.txt", "5 lists.txt", "6 program.c"
"""

import sys

def main():
    usage = """Usage: \n append_order.py starting_number filename1 filename2 filename3..."""
    if len(sys.argv) < 2:
        print(usage)
    try:
        start_num = int(sys.argv[1])
        print(start_num)
        return
    except ValueError:
        print(usage)
        return

if __name__ == '__main__':
    main()