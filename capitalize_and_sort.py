#!/usr/bin/env python3
# encoding: UTF-8

import sys

def main():
    #print("Starting...")
    args = sys.argv
    if(len(args) < 2):
        exit("Provide more arguments!")  
    
    for file in args[1:]:
        #print(f"Reading: {file}...")
        out_lines = []
        try:
            with open(file, "r") as lines:
                for line in lines:
                    new_line = []
                    prev_eq_space = False
                    for letter in line:
                        if prev_eq_space and letter.islower():
                            letter = letter.upper()
                        if letter.isspace():
                            prev_eq_space = True
                        else:
                            prev_eq_space = False
                        #print(letter, end='')
                        new_line.append(letter)
                    new_line = ("".join(new_line)).strip() + '\n'
                    #print(line)
                    #print(new_line)
                    if new_line != "\n":
                        out_lines.append(new_line)
                out_lines = sorted(out_lines)
                # Uncomment below to make a new file:
                write_to_file(make_out_name(file), out_lines)
                # Uncomment below to change in place:
                #write_to_file(file, out_lines)
        except FileNotFoundError:
            print("Input file: {file} not found. Please confirm file name exists.")
    print("All done!")
    return


def write_to_file(out_file, lines):
    #print(f"Writing to: {out_file}...")
    try:
        with open(out_file, "x") as out:
            for line in lines:
                out.write(line.strip() + '\n')
    except FileExistsError:
        print(f"File {out_file} exists already! No changes commited.")
    return


def make_out_name(in_name):
    pos = in_name.rfind(".")
    suffix = ' - capitalized & sorted'
    if pos > 0:
        out_name = in_name[0:pos] + suffix + in_name[pos:]
    else:
        out_name = in_name + suffix
    return out_name


if __name__ == "__main__":
    main()