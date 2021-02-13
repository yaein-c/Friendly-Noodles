import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format( mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('Time is up!!')

# input time in seconds
# t = 60

# function call
# countdown(int(t))
