import calendar
import datetime
import sys


def leap(i):
    return (i % 4 == 0 and i % 100 != 0) or i % 400 == 0


def same_calendars(cur, start, end):
    cal = calendar.Calendar()
    a = []
    for year in range(start, end):
        if (leap(year) != leap(cur)) or year == cur:
            continue
        f = True
        for month in range(1, 13):
            for day, dw in cal.itermonthdays2(year, month):
                if day != 0:
                    dw2 = datetime.date(cur, month, day).weekday()
                    f &= (dw == dw2)
        if f:
            a.append(year)
    return a


if len(sys.argv) > 1:
    year = int(sys.argv[1])
else:
    year = datetime.datetime.now().year
if leap(year):
    print(f"{year} is leap year")
if len(sys.argv) > 3:
    start = int(sys.argv[2])
    end = int(sys.argv[3])
else:
    start, end = 1900, 2101
for y in same_calendars(year, start, end):
    print(y, end=" ")
