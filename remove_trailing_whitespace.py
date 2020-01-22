#!/usr/bin/env python3
# encoding: UTF-8

import sys, os, glob

def main():
    #print("Starting...")
    args = sys.argv
    if(len(args) < 2):
        exit("Provide more arguments!")
        #os.chdir("DirectoryName")
        #for file in glob.glob("*.txt"):
        #    args.append(file)
    print("Started parsing!")
    file_num = 0
    for file in args[1:]:
        #print(f"Reading: {file}...")
        try:
            with open(file, "r") as lines:
                file_num += 1
                out_lines = []
                for line in lines:
                    new_line = line.rstrip()
                    out_lines.append(new_line)
                # Uncomment below to make a new file:
                #write_to_file_overwrite(make_out_name(file), out_lines)
                # Uncomment below to change in place:
                write_in_place(file, out_lines)
                print(f"  File #{file_num} \"" + file + "\" parsed.")
        except FileNotFoundError:
            print("Input file: {file} not found. Please confirm file name exists.")
    print("All done!")
    return


def write_to_file(out_file, lines):
    #print(f"Writing to: {out_file}...")
    try:
        with open(out_file, "x") as out:
            for line in lines:
                out.write(line + '\n')
    except FileExistsError:
        print(f"File {out_file} exists already! No changes commited.")
    return


def write_to_file_overwrite(out_file, lines):
    try:
        with open(out_file, "w") as out:
            for line in lines:
                out.write(line + '\n')
    except IOError:
        print("IOError on file \"" + out_file + "\"!.")
    return


write_in_place = write_to_file_overwrite


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
