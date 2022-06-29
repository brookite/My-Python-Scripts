import os
import sys


def scan_directory(dirpath):
    results = set()
    dirpath = os.path.abspath(dirpath)
    if os.path.isdir(dirpath):
        for root, dirs, files in os.walk(dirpath):
            for file in files:
                path = os.path.relpath(os.path.join(root, file), dirpath)
                results.add(path)
    return results


if len(sys.argv) > 2:
    dir1 = scan_directory(sys.argv[1])
    dir2 = scan_directory(sys.argv[2])
    for element in dir1.difference(dir2):
        print(element)


