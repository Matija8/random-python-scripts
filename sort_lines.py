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
        try:
            with open(file, "r") as input:
                input = sorted(input)
                write_to_file(make_out_name(file), input)
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
    out_name = in_name[0:pos] + ' - sorted.' + in_name[pos+1:]
    return out_name


if __name__ == "__main__":
    main()