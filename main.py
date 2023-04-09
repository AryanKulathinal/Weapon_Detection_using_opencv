import cv2 as cv
import numpy as np
import pyttsx3

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

capture=cv.VideoCapture("explosive2.mp4")
guns_cascade=cv.CascadeClassifier("XML_files\guns_cascade.xml")
knives_cascade=cv.CascadeClassifier("XML_files\knives_cascade.xml")
explsvs_cascade=cv.CascadeClassifier("XML_files\explsvs_cascade.xml")

while True:

    #initiallizing the speech engine
    engine = pyttsx3.init()
    #reading frames from video
    isTrue,frame=capture.read()
    #resizing the frame
    resized=cv.resize(frame,(500,500))
    #converting to monochrome
    gray=cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
    gun_detected=False
    knife_detected=False
    explsvs_detected=False
    gun_detect=guns_cascade.detectMultiScale(gray,scaleFactor=5,minNeighbors=3)
    knives_detect=knives_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    explsvs_detect=explsvs_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=50)
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
