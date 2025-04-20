import PyPDF2
import sys

# index 0 is the file_name
inputs = sys.argv[1:] #from index 1 to last

def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger() #object creation
    for pdf in pdf_list:
        print (f'added {pdf}')
        merger.append(pdf)
    merger.write('PDF_processing\\combined.pdf')

pdf_combiner(inputs)