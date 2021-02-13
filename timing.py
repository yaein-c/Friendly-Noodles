import time
from easygui import integerbox

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

def usertimeinput():
    value = integerbox("Please enter time in minutes to save butt:", "Timer length", None, 1, 25)
    value = value * 60  # change to seconds for cpuntdown function
    return value

    #while True:
    #     try:
    #        value = integerbox("Please enter time in minutes to save butt:", "Timer length", None, 1, 25)
    #        #value = int(input("Please enter time in minutes to save butt:\n"))
    #        value = value * 60
    #       break
    #     except:
    #        print("That's not a valid option!")
