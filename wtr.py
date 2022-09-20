import PyPDF2
import sys

inputs=sys.argv[1:]
print(inputs)
print(sys.argv)
template=PyPDF2.PdfFileReader(open(inputs[0],'rb'))
watermark=PyPDF2.PdfFileReader(open(inputs[1],'rb'))
output=PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
	page=template.getPage(i)
	page.mergePage(watermark.getPage(0))
	output.addPage(page)

	with open('watermarked_output2.pdf','wb') as file:
		output.write(file)