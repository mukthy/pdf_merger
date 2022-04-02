import PyPDF2

files = PyPDF2.PdfFileReader(open("twopage.pdf", "rb"))
watermark = PyPDF2.PdfFileReader(open("wtr.pdf", "rb"))
new_pdf = PyPDF2.PdfFileWriter()


pages = int(files.getNumPages())


for i in range(pages):
    page = files.getPage(i)
    print(i)
    watermark_page = watermark.getPage(0)
    page.mergePage(watermark_page)
    new_pdf.addPage(page)
    new_pdf.write(open('watermarked.pdf', 'wb'))
