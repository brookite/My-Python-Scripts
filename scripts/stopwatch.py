import time


if __name__ == "__main__":
    start = time.time()
    flag1 = start
    flag2 = 0
    print("Stopwatch\n")
    print("""Команды:
        :q - выйти
        :s - остановить таймер
        :t - всего времени прошло
        """)
    while True:
        flag = input("Нажмите Enter или введите команду: ")
        if flag == ":q":
            quit()
        elif flag == ":t":
            seconds = int(time.time() - start)
            hours, minutes, seconds = seconds // 3600, (seconds % 3600) // 60, (seconds % 3600) % 60
            print("Прошло времени: {} часов {} минут {} секунд".format(hours, minutes, seconds))
        elif flag == ":s":
            stoptime = time.time()
            input("Нажмите Enter, чтобы возобновить секундомер")
            resumetime = time.time()
            start += int(stoptime - resumetime)
        else:
            flag2 = time.time()
            seconds = int(flag2 - flag1)
            flag1 = flag2
            hours, minutes, seconds = seconds // 3600, (seconds % 3600) // 60, (seconds % 3600) % 60
            print("Прошло времени: {} часов {} минут {} секунд".format(hours, minutes, seconds))

