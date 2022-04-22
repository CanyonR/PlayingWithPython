import time


def main():
    print("  Look what I can do: \033[1A")
    spinnerlist = ["-", "\\", "|", "/"]

    loopCount = 0
    while loopCount < 3:
        for icon in enumerate(spinnerlist):
            print('\033[22C' + spinnerlist[icon[0]], end="\r")
            time.sleep(0.3333333)
        loopCount += 1
    print("\033[K" + "You snooze you lose!")


if __name__ == '__main__':
    main()
