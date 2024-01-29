import speech_recognition as sr 
import pyttsx3
import webbrowser
import os 
import time
import pyautogui
from pygame import mixer
import tkinter as tk 
from tkinter import *
import keyboard

w = Tk()

w.title("Era - Voice Assistant")




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.setProperty('rate', 180)




def takeacommd():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening")
        mixer.init()
        mixer.music.load("mic start.mp3")
        mixer.music.play()  
        r.pause_threshold = 1
        audio = r.listen(source)
    
   
    try:
        print("Recognizing...")    
        mixer.init()
        mixer.music.load("recognize.mp3")
        mixer.music.play() 
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Unable to Recognize your voice.")  
        return "None"
    
    return query

def speak(cmd):
    engine.say(cmd)
    engine.runAndWait()


def process():
            
    query = takeacommd().lower()

    if 'utkarsh' in query:
        print(query)
        speak("helloa my dear utkarsh")
        speak("hello i am era version 2.0 how are you ")
    
    elif 'open youtube' in query:
        print(query)
        speak("ok wait for minute....")
        webbrowser.open("www.youtube.com")
    
    elif 'open chrome' in query:
        print(query)
        speak("ok wait for minute....")
        path =  "C:/Program Files/Google/Chrome/Application/chrome.exe"
        os.startfile(path)

    
    elif 'search' in query:
        print(query)
        # res = query.replace('hey', '')
        res = query.replace('search', '')
        
        des = res.replace('era', '')

        print(des)
        speak(f"ok i am searching {des} on google")
        webbrowser.open(f"https://www.google.com/search?q= {des} ")
        # webbrowser.open(des, new=0)

    elif 'open code' in query:
        print(query)
        path = "C:/Users/HP/AppData/Local/Programs/Microsoft VS Code/Code.exe"
        os.startfile(path)

    elif 'open word' in query:
        speak('opening word')
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Word 2010"
        os.startfile(path)

    elif 'open powerpoint' in query:
        speak('opening powerpoint')
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft PowerPoint 2010"
        os.startfile(path)
    
    elif 'open excel' in query:
        speak('opening excel')
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Excel 2010"
        os.startfile(path)

    elif 'open chrome' in query:
        speak('opening chrome')
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome"
        os.startfile(path)

    elif 'open paint' in query:
        speak('opening paint')
        
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Paint"
        os.startfile(path)


    elif 'open google' in query:
        speak('opening google')
        webbrowser.open("www.google.com")

    
    elif 'open spotify' in query:
        speak('opening spotify')
        webbrowser.open("www.spotify.com")


    elif 'scroll up' in query:
        print(query)
        speak("scrolloing up")
        pyautogui.scroll(300)
    
    elif 'scroll down' in query:
        print(query)
        speak("scrolloing down")
        pyautogui.scroll(-300)
    elif 'close' in query:
        print(query)
        speak("closing...")
        pyautogui.hotkey('ctrl', 'w')
    elif 'stop' in query:
        print(query)
        speak("stopping...")
        pyautogui.hotkey('space')
    elif 'exit' in query:
        print(query)
        speak("exit form this....")
        pyautogui.hotkey('alt','f4')
    elif 'enter' in query:
        print(query)
        speak('enter key pressing')
        pyautogui.press('enter')


w.geometry("380x560")
# w.minsize(300,500)
# w.maxsize(300,500)
w.resizable(width = False, height = False  )
w.config(bg="black")
lbl = Label(w, text="Era Voice Assistant", font=('console',12,"bold"), bg="green", fg="white")
lbl.place(x=110,y=20)

lbl1 = Label(w, text="Commands:", font=('console',12,"bold"), bg="white", fg="black")
lbl1.place(x=10,y=60)

lbl2 = Label(w, text="1)Search : For searching anything on Google.", font=('console',10,"bold"), bg="black", fg="white")
lbl2.place(x=10,y=90)

lbl3 = Label(w, text="2)Open <app> : app = Word,Excel,Powerpoint,VScode,etc. ", font=('console',10,"bold"), bg="black", fg="white")
lbl3.place(x=10,y=120)

lbl4 = Label(w, text="3)Scroll-Up/Down : Scrolling up and down.", font=('console',10,"bold"), bg="black", fg="white")
lbl4.place(x=10,y=150)

lbl5 = Label(w, text="4)Close/Exit : Close the tab/exit the application.", font=('console',10,"bold"), bg="black", fg="white")
lbl5.place(x=10,y=180)


btn = Button(w,text="Click Here",command= process,bg= "green", fg="white", font=('console', 10, "bold"), width= 10)
btn.place(x= 140, y=450)
w.config(bg="black")
btn = Button(w,text="Exit",command= exit,bg= "red", fg="white", font=('console', 12, "bold"), width= 10)
btn.place(x= 130, y=510)

def exit():
    print("exit")

keyboard.add_hotkey("F4",process)
w.mainloop()