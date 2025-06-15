import PyPDF2

# template = PyPDF2.PdfFileReader(open('superduper.pdf', 'rb'))
# watermark = PyPDF2.PdfFileReader(open('water.pdf', 'rb'))
# output = PyPDF2.PdfFileWriter()

# for i in range(template.getNumPages()):
#     page = template.getPage(i)  #start with first page
#     page.mergePage(watermark.getPage(0))  # start with first page
#     output.addPage(page) #add the watermarked page in object attributes

# This is the new way to do this:
template = PyPDF2.PdfReader(open('PDF_processing\\combined.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('PDF_processing\\wtr.pdf', 'rb'))
output = PyPDF2.PdfWriter()

#New way to do this:
for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)
 
with open('PDF_processing\\watermaked_output.pdf', 'wb') as outputFile:
    output.write(outputFile)
    

 


 
 

 


 