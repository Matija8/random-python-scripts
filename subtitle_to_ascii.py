#!/usr/bin/env python3
# coding: UTF-8

import sys
import codecs
import re

mapping = {
    'ć': 'c', 'æ': 'c',     # ć
    'Ć': 'C',               # Ć
    'č': 'c', 'è': 'c',     # č
    'Č': 'C', 'È': 'C',     # Č
    'đ': 'dj', 'ð': 'dj',   # đ
    'Đ': 'Dj',              # Đ
    'š': 's',               # š
    'Š': 'S',               # Š
    'ž': 'z',               # ž
    'Ž': 'Z',               # Ž
    }

mapping = dict((re.escape(k), v) for k, v in mapping.items())
pattern = re.compile("|".join(mapping.keys()))


def main():
    args = sys.argv
    if len(args) < 2:
        exit("Provide more arguments!")
    for file in args[1:]:
        to_ascii(file)


def to_ascii(path):
    try:
        f = codecs.open(path, encoding='latin-1')
        contents = f.read()

        contents = pattern.sub(lambda m: mapping[re.escape(m.group(0))], contents)

        print(contents)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
