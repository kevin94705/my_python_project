import cv2
import time
import datetime
import os
import sys
import socket
nameData=""
def send_filename():   
    socket02 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INET:默認IPv4, SOCK_STREAM:TCP
    socket02.connect(address)  # 用來請求連接遠程服務器
    ##################################
    # 開始傳輸
    print('start send text')    
    while True:
        nameData = fileid
        socket02.sendall(bytes(nameData,encoding="utf8"))#取得文字送出文字
        prdata = str(socket02.recv(1024),encoding="utf8")
        img_name = prdata       
        break
    socket02.close()  # 關閉
    print('client close')
    time.sleep(0.1)
    send_img()

def send_img():
    socket02 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INET:默認IPv4, SOCK_STREAM:TCP    
    socket02.connect(address)
    ##################################
    # 開始傳輸
    print('start send image')
    imgFile = open(nameData, "rb")
    while True:
        imgData = imgFile.readline(5120)
        if not imgData:
            
            break  # 讀完檔案結束迴圈       
        socket02.send(imgData)    
    
    imgFile.close()

    print('transmit end')
    
    ##################################
    socket02.close()  # 關閉
    print('client close')
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
            send_filename()
            time.sleep(3600)
        else:
            time.sleep(10)
            continue
    except KeyboardInterrupt:
        print('close')
        break
