#!/usr/bin/bash
echo ========= required arg
python3 pdfcrop.py

echo ========= help
python3 pdfcrop.py -h

echo ========= general
python3 pdfcrop.py --input in.pdf --output out.pdf --top 10 --bottom 10 --left 10 --right 10 --gutter 10

echo ========= gutter only
python3 pdfcrop.py --input in.pdf --output gutter.pdf --gutter 30

echo ========= test stop
