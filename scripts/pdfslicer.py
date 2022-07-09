from PyPDF2 import PdfWriter, PdfReader
import argparse
import os
import sys


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("path")
    argparser.add_argument("sliceinfo", nargs="+")
    args = argparser.parse_args()

    if os.path.exists(args.path):
        file = open(args.path, "rb")
        pdf = PdfReader(file)

        total_pages = len(pdf.pages)
        print("Total pages:", total_pages)

        if args.sliceinfo[0] == "info":
            file.close()
            sys.exit(0)

        targetfile = open("sliced.pdf", "wb")
        targetpdf = PdfWriter()
        page_written = 0

        for slice in args.sliceinfo:
            slice = slice.split(":")
            if len(slice) == 3:
                start = int(slice[0])
                stop = int(slice[1])
                if slice[2].isdigit():
                    step = int(slice[2])
                    bookmark = None
                else:
                    bookmark = slice[2]
                    step = 1
            elif len(slice) == 4:
                start = int(slice[0])
                stop = int(slice[1])
                step = int(slice[2])
                bookmark = slice[3]
            elif len(slice) == 2:
                start = int(slice[0])
                stop = int(slice[1])
                step = 1
                bookmark = None

            if bookmark:
                print("Adding bookmark:", bookmark)
                targetpdf.add_bookmark(bookmark, page_written)

            for i in range(start, stop + 1, step):
                if i >= total_pages or i < 0:
                    continue
                page = pdf.pages[i]
                targetpdf.add_page(page)
                page_written += 1

        targetpdf.write(targetfile)
        targetfile.close()
        file.close()

        print("Written page count:", page_written)
    else:
        print("File not found")
