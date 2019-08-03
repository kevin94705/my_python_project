import socket
import time
import os
# host = socket.gethostname()
# port = 5000
host = '163.17.9.117'  # 對server端為主機位置
port = 48763

workpath=str(os.getcwd())

address = (host, port)
img_name=""
def send_filename():   
    socket02 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INET:默認IPv4, SOCK_STREAM:TCP
    socket02.connect(address)  # 用來請求連接遠程服務器
    ##################################
    # 開始傳輸
    print('start send text')    
    while True:
        nameData = "P_20190314_105629_90.jpg"
        socket02.sendall(bytes(nameData,encoding="utf8"))#取得文字送出文字
        prdata = str(socket02.recv(1024),encoding="utf8")
        img_name = prdata       
        break
    socket02.close()  # 關閉
    print('client close')
    send_img()
def send_img():
    socket02 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INET:默認IPv4, SOCK_STREAM:TCP    
    socket02.connect(address)
    ##################################
    # 開始傳輸
    print('start send image')
    imgFile = open(workpath+"\P_20190314_105629_90.jpg", "rb")
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
    time.sleep(5)
    

def get_json():
    socket02 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # AF_INET:默認IPv4, SOCK_STREAM:TCP    
    socket02.connect(address)
    while True:
        keys = "P_20190314_105629_90.jpg"
        socket02.sendall(bytes(keys,encoding="utf8"))#取得文字送出文字
        prdata = str(socket02.recv(1024),encoding="utf8")
        print(prdata)
        break
    socket02.close()
    return print('suc')

if __name__ == "__main__":
    send_filename()
    