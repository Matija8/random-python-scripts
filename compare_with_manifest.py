#! /usr/bin/env python3
# encoding: UTF-8

import os
import sys

def main():
    if len(sys.argv) < 3:
        exit('Error: Need a file name and a folder name.')
    compare_folder_and_txt(sys.argv[1], sys.argv[2])

def compare_folder_and_txt(txt_path, folder_path):
    files_in_folder = set()
    files_in_txt = set()

    get_from_folder(files_in_folder, folder_path)
    get_from_txt(files_in_txt, txt_path)
    print(len(files_in_txt))
    print(len(files_in_folder))

    diff1 = files_in_folder - files_in_txt
    print(len(diff1))

    diff2 = files_in_txt - files_in_folder
    print(len(diff2))

    #print_sorted_set(diff1)
    #print_sorted_set(diff2)


def get_from_folder(_set, _folder):
    for _, _, filenames in os.walk(_folder):
        for file in filenames:
            name = file.split('.')[0]
            _set.add(name)


def get_from_txt(_set, _txt):
    try:
        with open(_txt, 'r') as f:
            for line in f:
                line = line.strip()
                if len(line) > 0:
                    _set.add(line)
    except Exception as e:
        print(e)


def print_sorted_set(_set):
    set_as_list = list(_set)
    set_as_list.sort()
    for name in set_as_list:
        print(name)


if __name__ == '__main__':
    main()
