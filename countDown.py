import time

def countDown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\n")
        time.sleep(1)
        t -= 1

    print('Timer completed.')

t = int(input('Enter time in seconds: '))

countDown(t)
