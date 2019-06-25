import cv2
import time
import datetime
import os
import sys
import socket

while True:
    host = '163.17.9.117'  # 對server端為主機位置
    port = 5555
    address = (host, port)
    try:
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            fileid=datetime.datetime.now().strftime("%Y_%m_%d %H:%M:%S")+"jpg"
            cap.set(3,1280)
            cap.set(4,720)
            ret,frame = cap.read()
            cv2.imwrite(fileid,frame)       
            cap.release()
            cv2.destroyAllWindows()
            print("piced")
            
            time.sleep(3600)
        else:
            time.sleep(10)
            continue
    except KeyboardInterrupt:
        print('close')
        break
