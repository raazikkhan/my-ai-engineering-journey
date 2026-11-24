from PyPDF2 import PdfWriter

merger = PdfWriter()

# To Store all pdfs
pdfs = []

# User Input
user  = int(input("How many Pdf's do you want to merge?: "))

#looping through how many user wants pdf
for i in range(0, user):
    name = input(f"Enter the name of pdf {i + 1}: ")
    pdfs.append(name)

for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()