import time
numbers = iter[12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i%5:
        print(i)
    elif i>150:
            i=next(numbers)
    elif i>500:
                print("stop")
    else:
        print("ok")
