import cv2 as cv
import numpy as np

def textGenerator(text,frame,cascade) :
    for(x,y,w,h) in cascade:
            rectPt1=(x,y)
            rectPt2=(x+w,y+h)
            rectcolor=(0,0,255)
            result=cv.rectangle(frame,rectPt1,rectPt2,rectcolor,thickness=3)
            textPt=(x+2,y+10)
            textFont=cv.FONT_HERSHEY_SIMPLEX
            textColor=(255,255,255)
            boxPt1=(x,y)
            boxPt2=(x+w//2,y+h//7)
            cv.putText(frame,text,textPt,textFont,0.5,textColor,thickness=2)

capture=cv.VideoCapture("explosive1.mp4")
guns_cascade=cv.CascadeClassifier("guns_cascade.xml")
knives_cascade=cv.CascadeClassifier("knives_cascade.xml")
explsvs_cascade=cv.CascadeClassifier("explsvs_cascade.xml")

while True:
    isTrue,frame=capture.read()
    #resizing the frame
    resized=cv.resize(frame,(500,500))
    #converting to monochrome
    gray=cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
    gun_detected=False
    knife_detected=False
    explsvs_detected=False
    gun_detect=guns_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
    knives_detect=knives_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=7)
    explsvs_detect=explsvs_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=20)
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
    #Press q to exit window
    if cv.waitKey(25) & 0xFF == ord('q') :
        break
    
capture.release()
cv.destroyAllWindows()
        



