from PyPDF2 import PdfMerger
import argparse
import os

if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("path")
    argparser.add_argument("--sort-type", action="store")
    argparser.add_argument("--no-bookmark", action="store_true")
    args = argparser.parse_args()

    if os.path.isdir(args.path):
        dest = "merged.pdf"
        merger = PdfMerger()
        filelist = os.listdir(args.path)
        if not args.sort_type:
            key = None
        elif args.sort_type == "date":
            key = lambda x: os.path.getmtime(os.path.join(args.path, x))
        elif args.sort_type == "prefix":
            key = lambda x: int(x.split("_")[0])
        filelist.sort(key=key)
        for file in filelist:
            if os.path.splitext(file)[-1] == ".pdf":
                bookmark = file.replace(".pdf", "") if \
                    not args.no_bookmark else None
                print(f"Merging: {file}")
                merger.append(
                    os.path.join(args.path, file),
                    outline_item=bookmark
                )
        print("Writing to result PDF File...")
        merger.write(dest)
        merger.close()
        print("Done!")
    else:
        print("Invalid path")

