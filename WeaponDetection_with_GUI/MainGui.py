import cv2 as cv
import numpy as np
import pyttsx3
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk,Image

def textGenerator(text,frame,cascade) :
    for(x,y,w,h) in cascade:
            rectPt1=(x,y)
            rectPt2=(x+w,y+h)
            rectcolor=(0,0,255)
            result=cv.rectangle(frame,rectPt1,rectPt2,rectcolor,thickness=3)
            textPt=(x+2,y+10)
            textFont=cv.FONT_HERSHEY_SIMPLEX
            textColor=(255,255,255)
            cv.putText(frame,text,textPt,textFont,0.5,textColor,thickness=2)

def choose_file():
    file_path =  filedialog.askopenfilename()
    capture = cv.VideoCapture(file_path)
    detect_weapon(capture)

def open_camera():
    capture = cv.VideoCapture(0)
    detect_weapon(capture)

def detect_weapon(capture):
    guns_cascade=cv.CascadeClassifier("XML_files\guns_cascade.xml")
    knives_cascade=cv.CascadeClassifier("XML_files\knives_cascade.xml")
    explsvs_cascade=cv.CascadeClassifier("XML_files\explsvs_cascade.xml")
    while True:
        engine = pyttsx3.init()
        isTrue,frame=capture.read()
        resized=cv.resize(frame,(500,500))
        gray=cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
        gun_detected=False
        knife_detected=False
        explsvs_detected=False
        gun_detect=guns_cascade.detectMultiScale(gray,scaleFactor=5,minNeighbors=3)
        knives_detect=knives_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=7)
        explsvs_detect=explsvs_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=75)
        if len(gun_detect) != 0 :
            gun_detected=True
        if gun_detected :
            textGenerator("GUN",resized,gun_detect)        
        if len(knives_detect) != 0:
            knife_detected=True
        if knife_detected :
            textGenerator("BLADE", resized, knives_detect)
        if len(explsvs_detect) != 0:
            explsvs_detected=True
        if explsvs_detected:
            textGenerator("EXPLOSIVE", resized, explsvs_detect)
        cv.imshow("Weapon Detector",resized)
        if gun_detected or knife_detected or explsvs_detected :
            engine.say("Weapons Detected!")
            engine.runAndWait()
        #Press q to exit window
        if cv.waitKey(20) & 0xFF == ord('q') :
            break

    capture.release()
    cv.destroyAllWindows()

root = tk.Tk()
root.title("CCTV based weapon detection")
root.geometry("500x300")
image=Image.open("Back.jpeg")
resized_image = image.resize((500, 300), Image.ANTIALIAS)
bg_image = ImageTk.PhotoImage(resized_image)
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

label = tk.Label(root, text="CCTV based weapon detection", font=("Arial Bold", 20), fg="white", bg="black")
label.pack(pady=20)

file_button = tk.Button(root, text="Select file", command=choose_file)
file_button.pack(pady=10)
camera_button = tk.Button(root, text="Open camera", command=open_camera)
camera_button.pack(pady=10)
root.mainloop()