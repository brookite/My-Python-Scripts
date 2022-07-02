import argparse
import os
import pyvcard


def merge(root, files: list):
    vset = pyvcard.vCardSet()
    for file in files:
        file = os.path.join(os.path.abspath(root), file)
        if os.path.splitext(file)[-1] == ".vcf":
            try:
                vcard = pyvcard.openfile(file, encoding="utf-8").vcards()
                vset.update(vcard)
            except Exception:
                pass
    with open("out.vcf", "w", encoding="utf-8") as fobj:
        fobj.write(vset.repr_vcard())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Many vcard files to one file')
    parser.add_argument('input_dir', type=str, help='Input dir with vcards')
    args = parser.parse_args()
    if os.path.exists(args.input_dir) and os.path.isdir(args.input_dir):
        merge(args.input_dir, os.listdir(args.input_dir))
    else:
        print("Invalid path")
