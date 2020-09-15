# splittotext
Simple add-on for pdftotext that splits each page of a PDF into its own, individual text file, formatted as pagenum_PDFfile.pdf.
Useful when combined with grep to identify specific page numbers that a target word or phrase appear on within a PDF. Consider further utilization with PDFtk.

Usage:  ./splittotext.py <PDF-file> <int-number-of-pages>
Output: Creates a new directory, OrigPDFName_pdf, containing each of the PDF's page numbers as text files.

Requires pdftotext, available via https://github.com/freedesktop/poppler.


Example:
-------
![alt text](https://github.com/kampji/splittotext/blob/master/example.png)
