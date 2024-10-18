# PDF Crop
crops a PDF file

## Usage
usage: pdfcrop [-h] --input INPUT [--output OUTPUT]
               [--top TOP] [--bottom BOTTOM] [--left LEFT] [--right RIGHT]
               [--gutter GUTTER]

crops a pdf file

options:
  -h, --help       show this help message and exit
  --input INPUT    a PDF file to read
  --output OUTPUT  a PDF file to write, default=out.pdf
  --top TOP        crop amount from the top, default=10
  --bottom BOTTOM  crop amount from the bottom, default=10
  --left LEFT      crop amount from the left, default=10
  --right RIGHT    crop amount from the right, default=10
  --gutter GUTTER  crop amount for the gutter, default=10

unit of crop amount is 1 mm