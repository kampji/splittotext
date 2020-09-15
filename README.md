# splittotext
Simple add-on for pdftotext that splits each page of a PDF into its own, individual text file, formatted as pagenum_PDFfile.pdf.
Useful when combined with grep to identify specific page numbers that a target word or phrase appear on within a PDF. Consider further utilization with PDFtk.

Usage:  ./splittotext.py <PDF-file> <int-number-of-pages>
Output: Creates a new directory, OrigPDFName_pdf, containing each of the PDF's page numbers as text files.

Requires pdftotext, available via https://github.com/freedesktop/poppler.


Example:
-------
user@localhost:/mnt/hgfs/KaliShared/pdfs/example$ ls
nistspecialpublication800-115.pdf  splittotext.py
user@localhost:/mnt/hgfs/KaliShared/pdfs/example$ ./splittotext.py nistspecialpublication800-115.pdf 80
user@localhost:/mnt/hgfs/KaliShared/pdfs/example$ ls
nistspecialpublication800-115.pdf  nistspecialpublication800-115_pdf  splittotext.py
user@localhost:/mnt/hgfs/KaliShared/pdfs/example$ cd nistspecialpublication800-115_pdf/
user@localhost:/mnt/hgfs/KaliShared/pdfs/example/nistspecialpublication800-115_pdf$ ls -rt
1_nistspecialpublication800-115.pdf.txt   11_nistspecialpublication800-115.pdf.txt  24_nistspecialpublication800-115.pdf.txt  43_nistspecialpublication800-115.pdf.txt
9_nistspecialpublication800-115.pdf.txt   10_nistspecialpublication800-115.pdf.txt  23_nistspecialpublication800-115.pdf.txt  80_nistspecialpublication800-115.pdf.txt
8_nistspecialpublication800-115.pdf.txt   42_nistspecialpublication800-115.pdf.txt  61_nistspecialpublication800-115.pdf.txt  79_nistspecialpublication800-115.pdf.txt
7_nistspecialpublication800-115.pdf.txt   41_nistspecialpublication800-115.pdf.txt  60_nistspecialpublication800-115.pdf.txt  78_nistspecialpublication800-115.pdf.txt
6_nistspecialpublication800-115.pdf.txt   40_nistspecialpublication800-115.pdf.txt  59_nistspecialpublication800-115.pdf.txt  77_nistspecialpublication800-115.pdf.txt
5_nistspecialpublication800-115.pdf.txt   39_nistspecialpublication800-115.pdf.txt  58_nistspecialpublication800-115.pdf.txt  76_nistspecialpublication800-115.pdf.txt
4_nistspecialpublication800-115.pdf.txt   38_nistspecialpublication800-115.pdf.txt  57_nistspecialpublication800-115.pdf.txt  75_nistspecialpublication800-115.pdf.txt
3_nistspecialpublication800-115.pdf.txt   37_nistspecialpublication800-115.pdf.txt  56_nistspecialpublication800-115.pdf.txt  74_nistspecialpublication800-115.pdf.txt
2_nistspecialpublication800-115.pdf.txt   36_nistspecialpublication800-115.pdf.txt  55_nistspecialpublication800-115.pdf.txt  73_nistspecialpublication800-115.pdf.txt
22_nistspecialpublication800-115.pdf.txt  35_nistspecialpublication800-115.pdf.txt  54_nistspecialpublication800-115.pdf.txt  72_nistspecialpublication800-115.pdf.txt
21_nistspecialpublication800-115.pdf.txt  34_nistspecialpublication800-115.pdf.txt  53_nistspecialpublication800-115.pdf.txt  71_nistspecialpublication800-115.pdf.txt
20_nistspecialpublication800-115.pdf.txt  33_nistspecialpublication800-115.pdf.txt  52_nistspecialpublication800-115.pdf.txt  70_nistspecialpublication800-115.pdf.txt
19_nistspecialpublication800-115.pdf.txt  32_nistspecialpublication800-115.pdf.txt  51_nistspecialpublication800-115.pdf.txt  69_nistspecialpublication800-115.pdf.txt
18_nistspecialpublication800-115.pdf.txt  31_nistspecialpublication800-115.pdf.txt  50_nistspecialpublication800-115.pdf.txt  68_nistspecialpublication800-115.pdf.txt
17_nistspecialpublication800-115.pdf.txt  30_nistspecialpublication800-115.pdf.txt  49_nistspecialpublication800-115.pdf.txt  67_nistspecialpublication800-115.pdf.txt
16_nistspecialpublication800-115.pdf.txt  29_nistspecialpublication800-115.pdf.txt  48_nistspecialpublication800-115.pdf.txt  66_nistspecialpublication800-115.pdf.txt
15_nistspecialpublication800-115.pdf.txt  28_nistspecialpublication800-115.pdf.txt  47_nistspecialpublication800-115.pdf.txt  65_nistspecialpublication800-115.pdf.txt
14_nistspecialpublication800-115.pdf.txt  27_nistspecialpublication800-115.pdf.txt  46_nistspecialpublication800-115.pdf.txt  64_nistspecialpublication800-115.pdf.txt
13_nistspecialpublication800-115.pdf.txt  26_nistspecialpublication800-115.pdf.txt  45_nistspecialpublication800-115.pdf.txt  63_nistspecialpublication800-115.pdf.txt
12_nistspecialpublication800-115.pdf.txt  25_nistspecialpublication800-115.pdf.txt  44_nistspecialpublication800-115.pdf.txt  62_nistspecialpublication800-115.pdf.txt
user@localhost:/mnt/hgfs/KaliShared/pdfs/example/nistspecialpublication800-115_pdf$ 
