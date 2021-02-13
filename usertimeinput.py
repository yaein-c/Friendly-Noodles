from easygui import integerbox

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