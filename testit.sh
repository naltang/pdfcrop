#!/usr/bin/bash
echo ========= required arg
./pdfcrop.py

echo ========= help
./pdfcrop.py -h

echo ========= general
./pdfcrop.py --input in.pdf --output out.pdf --top 10 --bottom 10 --left 10 --right 10 --gutter 10

echo ========= gutter only
./pdfcrop.py --input in.pdf --output gutter.pdf --gutter 30

echo ========= test stop
