import PyPDF2

pdfFile = open('Elite-Form.pdf','rb')
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)

page = reader.getPage(pageNumber=0)
page.extractText()
for pagenum in range(reader.numPages):
    print(reader.getPage(pagenum).extractTect())
