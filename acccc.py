import csv
import os

ans_dic={}
dir_path = os.getcwd()
file_arr = []


# 開啟答案CSV 檔案
with open('Allans.csv', newline='') as csvfile:    
    rows = csv.DictReader(csvfile)
    for row in rows:
        name=row["檔名"]
        ans=row["答案"]
        ans_dic[name]=ans

for filename in os.listdir(dir_path):
    if filename=='Allans.csv':
        pass
    elif filename.endswith(".csv"):                    
        file_arr.append(filename)


correct_persent_record=[]
for get_filename in file_arr:
    correct_count=0
    input_count=0
    correct_persent=0.0
    with open(get_filename,newline='') as resultfile:
        rrows = csv.DictReader(resultfile)
        for rrow in rrows:
                input_count+=1
                r_name=rrow["檔名"]
                r_ans=rrow["偵測數量"]  
                if  r_name in ans_dic.keys():
                    if r_ans == ans_dic[r_name]:
                        correct_count+=1
                        #print("檔名:"+get_filename+"讀取的檔的答案是:"+r_ans+"正確解答:"+ans_dic[r_name])
                    else:
                        continue
    correct_persent=(correct_count/input_count)
    correct_persent_record.append((correct_persent)*100)
print(len(correct_persent_record))
print(sum(correct_persent_record)/len(correct_persent_record))
x=[]
for i in range(len(correct_persent_record)):
    x.append(i)
print(correct_persent_record)
'''
import numpy as np
import matplotlib.pyplot as plt

l1=plt.plot(x,correct_persent_record,'r--',label='type1')
plt.show()
'''