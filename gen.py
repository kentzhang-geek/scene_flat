# -*- coding: utf-8 -*-
import os
import sys
import shutil

# usage: python gen.py <language>
# example: python gen.py cpp
# support: cpp c rust
# special: all -> means generate all languages' code
# the code will bi in ./generated/<language>/

if len(sys.argv) < 2:
    print("usage: python gen.py <language>")
    print("example: python gen.py cpp")
    print("support: cpp c rust")
    print("special: all -> means generate all languages' code")
    exit(0)

# collect files in fbs/
def collect_files():
    files = []
    for root, dirs, filenames in os.walk("./fbs/"):
        for filename in filenames:
            files.append(filename)
    return files

def gen(language):
    shutil.rmtree("./generated/%s" % language)
    files = collect_files()
    for file in files:
        os.system("flatc --%s -o ./generated/%s --gen-object-api --filename-suffix \"\" ./fbs/%s" % (language, language, file))

language_list = ['cpp', 'c', 'rust']

lan = sys.argv[1].replace('-', '')
if lan == 'all':
    for language in language_list:
        gen(language)
elif lan in language_list:
    gen(sys.argv[1])
