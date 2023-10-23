import datetime
import os
import argparse
import random
import pickle


DELTA = 900


def walk_files(root_dir, formats=[]):
    files_result = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            path = os.path.abspath(os.path.join(root, file))
            ext = os.path.splitext(path)[1]
            if ext.startswith("."):
                ext = ext[1:]
            if not len(formats) or ext in formats:
                files_result.append(path)
    return files_result


formats = ["pdf"]
def main(root, formats, count):
    path = os.path.dirname(__file__)
    pkl = os.path.join(path, "filerand_files.pkl")
    required_update = True
    if os.path.exists(pkl):
        with open(pkl, "rb") as fobj:
            filestruct = pickle.load(fobj)
            if datetime.datetime.now().timestamp() - filestruct["timestamp"] < DELTA \
                and filestruct["formats"] == formats:
                files = filestruct["files"]
                required_update = False
    if required_update:
        files = walk_files(root, formats=formats)
        with open(pkl, "wb") as fobj:
            pickle.dump({"files": files, "formats": formats, "timestamp": datetime.datetime.now().timestamp()}, fobj)
    random.shuffle(files)
    return files[:count]


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(description="Random file selecting from directory tree")
    argparser.add_argument("root", help="Root directory")
    argparser.add_argument("-c", type=int, nargs=1, help="Required count of files", metavar="Count")
    argparser.add_argument("-f", type=str, nargs=1, help="Required count of files", metavar="Formats")
    args = argparser.parse_args()
    count = args.c[0] if args.c else 1
    formats = args.f[0].split(",") if args.f else []
    result = main(args.root, formats, count)
    for path in result:
        print(path)
