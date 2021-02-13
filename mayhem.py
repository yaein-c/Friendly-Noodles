from webbrowser import open
from easygui import msgbox
import time


def websiteopener():
    open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    time.sleep(8)  # to let rickroll load
    open("https://www.google.com")
    open("https://www.yahoo.com")
    open("https://www.netflix.com")
    open("https://www.amazon.com")
    open("https://www.apple.com")
    open("https://www.nfl.com")
    open("https://www.duolingo.com")
    open("https://www.instagram.com")
    open("https://www.ed.ac.uk")
    open("https://youtu.be/L_jWHffIx5E?t=36")  # all star


def popupopener():
    msgbox("This is a message!!", title="Title")
    msgbox("Good evening you shouldn't be sitting for too long", title="STAND UP")
    msgbox("Your butt is sore", title="Declaration")
    msgbox("We are trying to help you", title="Peacefulness")
    msgbox("Thank you for saving your butt it means a lot", title="Happiness noises")

