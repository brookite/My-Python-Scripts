import argparse
import os
import pyvcard


def view(file):
    vset = pyvcard.openfile(file, encoding="utf-8").vcards()
    return pyvcard.convert(vset).csv().permanent_result()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='vCard to CSV')
    parser.add_argument('file', type=str, help='Input file with vcards')
    parser.add_argument('-f', type=str, help='Filename to save')
    args = parser.parse_args()
    if os.path.exists(args.file):
        if not args.f:
            print(view(args.file))
        else:
            f = open(args.f, "w", encoding="utf-8")
            f.write(view(args.file))
            f.close()
    else:
        print("Invalid path")
