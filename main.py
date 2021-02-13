# from timing import countdown the old timer
from timer import submit
from mayhem import websiteopener, popupopener
from viewer import usertimeinput, setanothertimer, endofsession

#countdown(usertimeinput()) this is for the timing.py use
#submit()
#websiteopener()
#popupopener()
#print("End check")


# this will be the main loop of program
while True:
    submit()
    websiteopener()
    popupopener()

    if setanothertimer()==False:
        break

endofsession()