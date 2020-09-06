#!/usr/bin/env python3
# encoding: UTF-8

import sys
from os.path import realpath, dirname
from os import chdir, walk
from typing import Set, Tuple, Union

def compare_with_manifest(manifest: str, folder: str) -> None:
    '''
    Take all lines from manifest (some_file.txt)
    and see how many of those items (lines) are present
    as files in folder "folder".
    '''
    # Set current working directory to this scripts directory.
    chdir(dirname(realpath(__file__)))

    folder_data = get_from_folder(folder)
    manifest_data, duplicates = get_from_txt(manifest)

    folder_extra = folder_data - manifest_data
    manifest_extra = manifest_data - folder_data


    print ('\nTerms not in folder:\n')
    print_sorted_set(manifest_extra)

    print('\nTerms not in manifest:\n')
    print_sorted_set(folder_extra)

    print('\nDuplicate manifest terms:\n')
    print_sorted_set(duplicates)


    print('\n--- Info ---')
    print('Manifest data:', len(manifest_data))
    print('Folder data:',  len(folder_data))
    print('Folder data not in Manifest:', len(folder_extra))
    print('Manifest data not in Folder:', len(manifest_extra))


def get_from_folder(folder: str) -> Set[str]:
    '''
    Return set containing file names from folder 'folder'
    with extension stripped.
    '''
    data = set()
    for _, _, filenames in walk(folder):
        for file in filenames:
            name = file.rsplit('.', 1)[0]
            data.add(name)
    return data


def get_from_txt(txt_file: str) -> Tuple[Set[str], Set[str]]:
    '''
    Return set containing lines from file txt_file
    with everything right of first '(' stripped,
    and set containing duplicated lines.
    '''
    # Two lines can be duplicates up to '(', but have important
    # extra info after '(' in each. We want to handly this manualy.
    data, duplicates = set(), set()
    try:
        with open(txt_file, 'r') as f:
            for line in f:
                name = (line.split('(', 1)[0]).strip()
                if name in data:
                    duplicates.add(name)
                data.add(name)
    except Exception as e:
        print('Unknown exception!', e, sep='\n')
    return data, duplicates


def print_sorted_set(data: Set[str], stream=sys.stdout) -> None:
    '''
    Prints set of strings in sorted order.
    '''
    for name in sorted(list(data)):
        print(name, file=stream)


def _main() -> None:
    ''' Main function. '''
    # You can specify manifest and folder here.
    manifest = None # type: Union[str, None]
    folder = None   # type: Union[str, None]

    usage = f'Usage: $ {__file__} manifest_name.txt folder_name'

    # Take args from sys.argv if args not set.
    if not manifest or not folder:
        if len(sys.argv) < 3:
            print('Not enough arguments given!')
            print(usage)
            return
        manifest = sys.argv[1]
        folder = sys.argv[2]
    compare_with_manifest(manifest, folder)

if __name__ == '__main__':
    _main()
