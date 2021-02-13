import webbrowser
import time
import easygui


def websiteopener():
    webbrowser.open_new("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    time.sleep(8)  #to let rickroll load
    webbrowser.open("https://www.google.com")
    webbrowser.open("https://www.yahoo.com")
    webbrowser.open("https://www.netflix.com")
    webbrowser.open("https://www.amazon.com")
    webbrowser.open("https://www.apple.com")
    webbrowser.open("https://www.nfl.com")
    webbrowser.open("https://www.duolingo.com")
    webbrowser.open("https://youtu.be/L_jWHffIx5E?t=36")  # all star
    webbrowser.open("https://www.instagram.com")
    webbrowser.open("https://www.facebook.com")
    webbrowser.open("https://www.ed.ac.uk")

def popupopener():
    easygui.msgbox("This is a message!!", title="Title")
    easygui.msgbox("Good evening you shouldn't be sitting for too long", title="STAND UP")
    easygui.msgbox("Your butt is sore", title="Declaration")
    easygui.msgbox("We are trying to help you", title="Peacefulness")
    easygui.msgbox("Thank you for saving your butt it means a lot", title="Happiness noises")