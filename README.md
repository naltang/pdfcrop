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

## Examples

1. The following command crops each page of ``org.pdf`` 20 mm and 15 mm from the left and the top respectively, and stores the cropped file to ``crop.pdf``

```
python3 pdfcrop.py --input org.pdf --output crop.pdf --left 20 --top 15
```

2. The following command crops ``org.pdf`` 10 mm from the left for odd pages, and 10 mm from the right for even pages, and stores the cropped file to ``crop.pdf``
```
python3 pdfcrop.py --input org.pdf --output crop.pdf --gutter 10
```

## Dependency
needs pypdf

## Limitations
1. cannot crop encrypted PDFs.
2. possible loss of information, such as notes and attached files, etc.
3. changes PDF version to 1.3 for the output file, due to pypdf limitation.

## License
MIT license
