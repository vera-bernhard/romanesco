#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Machine Translation
# Assignment 4
import sys
import lxml.etree as ET
from pathlib import Path

def extract(fn):
    '''Get Swiss German Text from '''
    for _, elem in ET.iterparse(fn):
        if elem.tag == 'u':
            yield '\n'
        if elem.tag == 'w':
            yield elem.text
            yield ' '
        
def main():
    currentDirectory = Path('./processed')
    currentPattern = "*.xml"

    
    with open('outfile.txt', 'w+', encoding='utf-8') as outfile:
        for currentFile in currentDirectory.glob(currentPattern):
            file = str(currentFile)
            for elem in extract(file):
                outfile.write(elem)
    
    

if __name__ == "__main__":
    main()