from timer import submit
from mayhem import websiteopener, popupopener
from viewer import setanothertimer, endofsession

#this is to test once
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