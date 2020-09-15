#!/usr/bin/python3
# splittotext.py
# Jill Kamperides, 20200908
# Splits each page of a PDF file into separate text files formatted as pagenum_PDFfile.pdf
# Requires pdftotext

import sys
import os

try:
    pdfname = sys.argv[1]
    pagenum = sys.argv[2]
    pdfdir = pdfname.replace(".pdf", "_pdf") # stores each PDF's text files in their own dir
    os.mkdir(pdfdir)
    for i in range(1, int(pagenum)+1):
        os.system("pdftotext -q -f " + str(i) + " -l " + str(i) + " " + pdfname + " " + ".//" + pdfdir + "//"  + str(i) + "_" + pdfname + ".txt")
except:
    print("Splits each page of a PDF file into separate text files formatted as pagenum_PDFfile.pdf")
    print("Usage: ./splittotext.py <PDF-file> <int-number-of-pages>")
