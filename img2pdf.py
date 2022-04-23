# pip install fpdf
import os, os.path
from fpdf import FPDF

valid_images = [".jpg",".gif",".png",".tga"]
imagelist = []
for f in os.listdir():
    ext = os.path.splitext(f)[1]
    if ext.lower() in valid_images:
        imagelist.append(f)

print(imagelist)       
pdf = FPDF()
# imagelist is the list with all image filenames

for image in imagelist:
    pdf.add_page()
    pdf.image(image)
pdf.output("yourfile.pdf", "F")
