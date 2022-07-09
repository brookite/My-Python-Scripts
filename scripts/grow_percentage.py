def percent_delta(basis, new):
    return ((100 * new) / basis) - 100


if __name__ == "__main__":
    prev = None
    while True:
        try:
            value = float(input(">> "))
            if prev is not None:
                percent = percent_delta(prev, value)
                print(round(percent, 2), "%", sep='')
            prev = value
        except Exception:
            print("Invalid data")
        except KeyboardInterrupt:
            break
