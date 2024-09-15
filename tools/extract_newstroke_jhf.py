#!/usr/bin/env python3

import ast
import sys


# Open the KiCAD source file contaning the font
# (give the file 'newstroke_font.cpp' as the only argument)
# read all lines
with open(sys.argv[1], 'r') as fp:
    cpp = fp.readlines()

# Find the first and last line of the font definition block
first = next(i for i,s in enumerate(cpp) if 'newstroke_font[]' in s)
last =  next(i for i,s in enumerate(cpp[first:], first) if '};' in s)
# Slice out the relevant lines and change c-style comments to
# python-style comments
lines = [l.replace('/*', '#') for l in cpp[first+2:last]]

# Join lines to form a string of correct python list syntax
py = '[' + ''.join(lines) + ']'
# Parse the python list
glyphs = ast.literal_eval(py)

# Print all glyphs in jhf file format
for i,glyph in enumerate(glyphs, 32):
    print(f'{i:5d}{len(glyph)//2:3d}{glyph}')
