#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Machine Translation
# Assignment 4

import sys

infile = sys.argv[1]

with open('archimed_plain.txt', 'w', encoding='utf-8') as outfile:
    with open(infile,'r',encoding='utf-8') as infile:
        for line in infile:
            if line =='\n':
                pass
            else:
                outfile.write(line)