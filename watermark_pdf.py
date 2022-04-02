import PyPDF2
import sys

files = sys.argv[1]
watermark = sys.argv[2]

pdf_files = PyPDF2.PdfFileReader(open(f"{files}", "rb"))
watermark_file = PyPDF2.PdfFileReader(open(f"{watermark}", "rb"))
new_pdf = PyPDF2.PdfFileWriter()


pages = int(pdf_files.getNumPages())


for i in range(pages):
    page = pdf_files.getPage(i)
    print(i)
    watermark_page = watermark_file.getPage(0)
    page.mergePage(watermark_page)
    new_pdf.addPage(page)
    new_pdf.write(open('watermarked.pdf', 'wb'))
