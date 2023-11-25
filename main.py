from deepface import DeepFace
import numpy as np
import csv
import cv2
import os
import pandas as pd
import threading
cap=cv2.VideoCapture(0)
face_cap=cv2.CascadeClassifier("C:/Users/naman/AppData/Local//Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
count=0
personName="Naman Bansal"
def showImg():
    while True:
        ret,frame=cap.read()
        faces=face_cap.detectMultiScale(
            cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY),
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30,30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for x,y,w,h in faces:
            cv2.putText(frame,text=personName,fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.8,color=(0,255,0),org=(x,y-6),thickness=2)
            cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),thickness=3,color=(0,255,255))
        cv2.imshow("camera",frame)
        if cv2.waitKey(1) & 0xFF == ord('x'): 
            break
    cap.release()
    cv2.destroyAllWindows()
    
def classifyImg():
    global personName   
    global count
    while True:
        ret,frame=cap.read()
        fileNam=f"myimg{count}.png"
        cv2.imwrite(fileNam, cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY))
        result=DeepFace.find(img_path=fileNam,db_path="./my_db",enforce_detection=False)
        df=pd.DataFrame(result[0],columns=["identity","source-X","source-y","source-w","source-h","Cosine"])
        print()
        if result:
            # print(f"The Result is {result[0]}")
            print(f"Type of Result is {df['identity']}")
            # name_of_person=df['identity'].split("/")[2]
            print(type(df['identity']))
            id_list=df['identity']
            if len(id_list)!=0:
                if len(id_list[0])!=0:
                    personName=id_list[0].split("/")[2][0:-4]
        os.remove(fileNam)
        if cv2.waitKey(1) & 0xFF == ord('x'): 
            break
    cap.release()
    cv2.destroyAllWindows()
t1=threading.Thread(target=showImg)
t2=threading.Thread(target=classifyImg)
t2.start()
t1.start()
