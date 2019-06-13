import cv2
import license_module as m     # 匯入自訂模組
import os
#取得py資料夾位置 

dir_path = os.getcwd()
file_arr = []

for filename in os.listdir(dir_path):
    if filename.endswith(".jpg"):                    
        file_arr.append(filename)
for img_name in file_arr:
    img = cv2.imread(img_name)
     # 讀取圖片
    text = m.get_license(img) 
    if   len(text)==8:
        p1=(text[0],text[1])
        p4=(text[4],text[5])
        cv2.rectangle(img, p1, p4, (0, 255, 0), 2)  # 進行車牌辨識
        cv2.imshow(img_name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    #print('車牌:', text)
 


