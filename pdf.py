import PyPDF2

with open("dummy.pdf", "rb") as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    print(page)
    print(page.rotateClockwise(90))
