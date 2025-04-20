import PyPDF2

# with open ('PyPDF2\\dummy.pdf', 'r') as file :
#     print (file)    #ok:  <_io.TextIOWrapper name='PyPDF2\\dummy.pdf' mode='r' encoding='cp1252'>
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages) #PdfReadWarning: PdfFileReader stream/file object is not in binary mode

# with open ('PyPDF2\\twopage.pdf', 'rb') as file :
#     print (file)    #ok:  <_io.TextIOWrapper name='PyPDF2\\dummy.pdf' mode='r' encoding='cp1252'>
#     reader = PyPDF2.PdfFileReader(file)
#     print(reader.numPages)  #output = 2
#     print(reader) # output = <PyPDF2.pdf.PdfFileReader object at 0x0000014A13DF41A0>

with open ('PyPDF2\\twopage.pdf', 'rb') as file :
    reader = PyPDF2.PdfFileReader(file) # object creation that reads file
    page = reader.getPage(0)   #get first page
    page.rotateCounterClockwise(90) # rotate the first page of the object

    writer = PyPDF2.PdfFileWriter() #object creation that writes into a file
    #only written in memory
    writer.addPage(page) #add rotated page attribute to the object
    
    # nested to create the file and write into a new file(not memory)
    # Using "w" to write, auto creates new file if doesn't exist
    with open ('PyPDF2\\tilt.pdf', 'wb') as new_file:
        writer.write(new_file)  # write the object(with rotated page) into the file