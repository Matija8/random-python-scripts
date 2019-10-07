#!/usr/bin/env python3
# encoding: UTF-8

import sys

def main():
    set_encoding = "UTF-8"
    lines = []
    for file_name in sys.argv[1:]:
        try:
            with open(file_name, "r+", encoding = set_encoding) as file:
                lines = file.readlines()
        except IOError as e:
            print(e)
            return None
        print(lines)
        try:
            with open(file_name, "w+", encoding = set_encoding) as file:
                i = 1
                for line in lines:
                    if i < 10:
                        line_number = '0' + str(i)
                    else:
                        line_number = str(i)
                    line = line_number + ' ' + line
                    file.write(line)
                    i += 1
                file.flush()
        except IOError as e:
            print(e)
            return None


    

if __name__ == "__main__":
    main()