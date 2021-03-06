#Contact Tracing App
# Create a python program that will read QRCode using your webcam
# You may use any online QRCode generator to create QRCode
# All personal data are in QRCode 
# You may decide which personal data to include
# All data read from QRCode should be stored in a text file including the date and time it was read

#Note: 
#Search how to generate QRCode
#Search how to read QRCode using webcam
#Search how to create and write to text file
#Your source code should be in github before Feb 19
#Create a demo of your program (1-2 min) and send it directly to my messenger.

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        global qrdata
        qrdata = obj.data.decode("utf-8")
        print("Reading data. Press escape key to stop camera")
  
    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
    
dataItems = qrdata.split("\r")
information = list(dataItems)

from datetime import date, datetime
currentTime = datetime.now()
timeString = currentTime.strftime("%d/%m/%Y %H:%M:%S")


sys.stdout = open("Data from QR Code.txt", "w")
print (information[0])
print (information[1])
print (information[2])
print (information[3])
print (information[4])
print (f"Date and time read:{timeString}")

sys.stdout.close()


