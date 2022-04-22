import time

print("Look what I can do: \033[1A")
spinnerlist = ["-", "\\", "|", "/"]

loopCount = 0
while loopCount < 3:
    for icon in range(len(spinnerlist)):
        print('\033[20C' + spinnerlist[icon], end="\r")
        time.sleep(0.3333333)
    loopCount += 1
print("\033[K" + "You snooze you lose!")
