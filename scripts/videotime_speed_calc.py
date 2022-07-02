import sys

def parse(time):
    return tuple(map(int, time.split(":")))


def seconds(timetuple):
    s = 0
    i = len(timetuple) - 1
    while i != -1:
        s += timetuple[i] * 60 ** abs(len(timetuple) - 1 - i)
        i -= 1
    return s


def to_time(seconds):
    h = int(seconds // 3600)
    seconds %= 3600
    m = int(seconds // 60)
    seconds %= 60
    s = int(seconds)
    return h, m, s


def calc(timestr, speed):
    speed = float(speed)
    timestr = seconds(parse(timestr))
    return to_time(timestr / speed)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        time = sys.argv[1]
        if len(sys.argv) > 2:
            speed = float(sys.argv[2])
        else:
            speed = 1
        r = ":".join(list(map(str, calc(time, speed))))
        print(f"Видео длится {time}")
        print(f"Вы посмотрите это видео за {r}")
    else:
        time = input("Введите длительность видео: ")
        speed = float(input("Введите скорость видео: "))
        r = ":".join(list(map(str, calc(time, speed))))
        print(f"Видео длится {time}")
        print(f"Вы посмотрите это видео за {r}")
