**Description:** A Python script to convert PDF files into a series of JPEG images, with each page of the PDF becoming a separate image. The script uses a file dialog box for file selection and the pdf2image library for conversion.

**README:**

# PDF-to-JPEG-Converter

PDF-to-JPEG-Converter is a Python-based utility that allows you to convert any PDF file into a series of JPEG images. Each page of the PDF becomes a separate image, allowing for easy manipulation, sharing, and usage of the content.

## Features
- File dialog box for easy file selection 
- Conversion of each PDF page into a separate JPEG image 
- Automatic saving of images into the same directory as the original PDF
- Clear filenames indicating the page number

## Usage
When the script is run, it prompts the user to select a PDF file through a file dialog box. If a PDF file is selected, the script uses the `convert_from_path` function from the `pdf2image` library to convert each page of the PDF into a separate image. The images are then saved into the same directory as the original PDF, with filenames indicating the page number. If no file is selected, the script simply prints "No file selected."

## Dependencies
This script requires the `pdf2image` library for the conversion process. 

## Installation
To install the `pdf2image` library, use the following pip command:
```
pip install pdf2image
```

## Future Improvements
This is a basic version of the script. Future updates may include batch conversions, quality settings for the output images, and additional file format support. 

## Contributing
Any contributions you make are greatly appreciated. If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again! 

## License
[MIT](https://choosealicense.com/licenses/mit/)