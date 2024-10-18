# PDF Crop
crops a PDF file

## Usage
```
usage: pdfcrop [-h] --input INPUT [--output OUTPUT]
               [--top TOP] [--bottom BOTTOM] [--left LEFT] [--right RIGHT]
               [--gutter GUTTER]

crops a pdf file

options:
  -h, --help       show this help message and exit
  --input INPUT    a PDF file to read
  --output OUTPUT  a PDF file to write, default=out.pdf
  --top TOP        crop amount from the top, default=0
  --bottom BOTTOM  crop amount from the bottom, default=0
  --left LEFT      crop amount from the left, default=0
  --right RIGHT    crop amount from the right, default=0
  --gutter GUTTER  crop amount for the gutter, default=0

unit of crop amount is 1 mm
```

## Example

```
pdfcrop --input org.pdf --output crop.pdf --left 20 --top 15
```
This crops ``org.pdf`` 10 mm from the left, 15 mm from the top, and stores the cropped file to ``crop.pdf``

```
pdfcrop --input org.pdf --output crop.pdf --gutter 10
```
This crops ``org.pdf`` 10 mm from the left for odd pages, and 10 mm from the right for even pages, and stores the cropped file to ``crop.pdf``

## Dependency
needs pypdf

## License
MIT license
