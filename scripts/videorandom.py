import argparse
import os
import subprocess
import random
import shelve

DATABASE = shelve.open("videorandom.db")

ALLOWED_FORMATS = [
    "mp3", "mp4", "aac", "wav", "ogg",
    "avi", "ts", "mpeg", "mpg", "amr",
    "flac", "mkv", "flv", "mpeg4", "opus",
    "wmv", "wma", "webm"
]


def get_length(filename):
    if filename in DATABASE:
        return DATABASE[filename]
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    length = float(result.stdout.decode("utf-8").split("\n")[0])
    store(filename, length)
    return length


def store(filename, length):
    DATABASE[filename] = length


def query(roots, eachduration=None):
    array = []
    total = 0
    for root in roots:
        for root, dirs, files in os.walk(os.path.abspath(root)):
            for file in files:
                file = os.path.join(root, file)
                if os.path.splitext(file)[-1][1:] in ALLOWED_FORMATS:
                    length = get_length(file)
                    if eachduration is None:
                        array.append([file, length])
                    elif length <= eachduration:
                        total += length
                        array.append([file, length])
    DATABASE.close()
    return array


def parse_time(string):
    if not string:
        return None
    else:
        string = string[0]
    t = 0
    buf = ""
    for i in range(len(string)):
        if string[i].isdigit():
            buf += string[i]
        else:
            if string[i] == "h":
                t += int(buf) * 3600
            elif string[i] == "m":
                t += int(buf) * 60
            else:
                t += int(buf)
            buf = ""
    return t


def main():
    args = argparse.ArgumentParser(description="Random video selection")
    args.add_argument("rootpath", type=str, nargs="+", help="Root path for video searching")
    args.add_argument("-c", type=int, nargs=1, help="Required count of files", metavar="Count")
    args.add_argument("-t", type=str, nargs=1, help="Total duration", metavar="Total duration")
    args.add_argument("-ed", type=str, nargs=1, help="Duration of each file", metavar="Each duration")
    parsed = args.parse_args()
    results = query(parsed.rootpath, parse_time(parsed.ed))
    random.shuffle(results)
    if parsed.c:
        count = parsed.c[0]
        if count <= len(results):
            results = results[:count]
    total = parse_time(parsed.t)
    k = 0
    for item in results:
        if total:
            if k + item[1] > total:
                break
        k += item[1]
        print(item[0])


if __name__ == '__main__':
    main()
