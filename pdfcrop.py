#!/usr/bin/env python3
import pypdf
import argparse

def main():
    args = parser.parse_args()

    FROM_MILLIMETER_TO_1_OVER_72_INCH = 72 / 25.4
    args.top = args.top * FROM_MILLIMETER_TO_1_OVER_72_INCH
    args.bottom = args.bottom * FROM_MILLIMETER_TO_1_OVER_72_INCH
    args.left = args.left * FROM_MILLIMETER_TO_1_OVER_72_INCH
    args.right = args.right * FROM_MILLIMETER_TO_1_OVER_72_INCH
    args.gutter = args.gutter * FROM_MILLIMETER_TO_1_OVER_72_INCH

    reader = pypdf.PdfReader(args.input)
    writer = pypdf.PdfWriter()
    writer.clone_reader_document_root(reader)
    for num_page in range(len(reader.pages)):
        if num_page % 2 == 0:
            left_gutter = args.gutter
            right_gutter = 0
        else:
            left_gutter = 0
            right_gutter = args.gutter
        page = reader.pages[num_page]
        newbox = page.mediabox
        newbox.left = page.mediabox.left + args.left + left_gutter
        newbox.right = page.mediabox.right - args.right - right_gutter
        newbox.top = page.mediabox.top - args.top
        newbox.bottom = page.mediabox.bottom + args.bottom
        page.mediabox = newbox
        writer.add_page(page)

    if reader.metadata is not None:
        writer.add_metadata(reader.metadata)

    f = open(args.output, "wb")
    writer.write(f)
    f.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.prog = "pdfcrop"
    parser.description = "crops a pdf file"
    parser.epilog="unit of crop amount is 1 mm"
    parser.add_argument("--input", required=True, help="a PDF file to read")
    parser.add_argument("--output", default="out.pdf", help="a PDF file to write, default=%(default)s")
    parser.add_argument("--top", type=float, default=0, help="crop amount from the top, default=%(default)s")
    parser.add_argument("--bottom", type=float, default=0, help="crop amount from the bottom, default=%(default)s")
    parser.add_argument("--left", type=float, default=0, help="crop amount from the left, default=%(default)s")
    parser.add_argument("--right", type=float, default=0, help="crop amount from the right, default=%(default)s")
    parser.add_argument("--gutter", type=float, default=0, help="crop amount for the gutter, default=%(default)s")
    main()
