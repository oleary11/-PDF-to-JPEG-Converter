import os
from pdf2image import convert_from_path
import tkinter as tk
from tkinter import filedialog

def convert_pdf_to_jpg(pdf_file_path, output_folder):
    images = convert_from_path(pdf_file_path)

    for page_num, image in enumerate(images):
        jpg_file_path = os.path.join(output_folder, f'page_{page_num}.jpg')
        image.save(jpg_file_path, 'JPEG')
        print(f'Page {page_num} saved as {jpg_file_path}')

def select_pdf_file():
    root = tk.Tk()
    root.withdraw() 

    file_path = filedialog.askopenfilename(
        title="Select a PDF file",
        filetypes=[("PDF files", "*.pdf")]
    )

    return file_path

pdf_file = select_pdf_file()
if pdf_file:
    output_folder = os.path.dirname(pdf_file)
    convert_pdf_to_jpg(pdf_file, output_folder)
else:
    print("No file selected.")
