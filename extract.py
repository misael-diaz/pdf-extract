#!/usr/bin/python3
"""
pdf-extract                                               May 03, 2025
author: @misael-diaz
source: extract.pdf

Automates the tedious task of extracting student names and their scores from a PDF.

Copyright (c) 2025 Misael Diaz-Maldonado
This file is released under the GNU General Public License version 2 only
as published by the Free Software Foundation.
"""

import os
import subprocess 

def extract_page(page):
    cmd=(
        f"gs -dBATCH -dNOPAUSE -dSAFER -sDEVICE=pdfwrite -sOutputFile={page}.pdf " +
        f"-dFirstPage={page} -dLastPage={page} {doc} 1>/dev/null 2>/dev/null"
    )
    os.system(cmd)
    return

def convert_text(page):
    cmd=f"pdftotext {page}.pdf"
    os.system(cmd)
    return

def get_name(page):
    ret = subprocess.run(
        ["sed", "-n", "2p", f"{page}.txt"], capture_output=True
    )
    name = str(ret.stdout.decode("utf-8")).strip("\n")
    return name

def get_score(page):
    ret = subprocess.run(
            ["sed", "-n", "26p", f"{page}.txt"], capture_output=True
    )
    score = str(ret.stdout.decode("utf-8")).strip("\n")
    return score


doc="doc.pdf"
pages=86

names = []
scores = []
for page in range(0, pages, 2):
    pagenum = page + 1
    extract_page(pagenum)
    convert_text(pagenum)
    name = get_name(pagenum)
    score = get_score(pagenum)
    names.append(name)
    scores.append(score)
    #print(f"{name} {score}")

for name in names:
    print(name)
for score in scores:
    print(score)
