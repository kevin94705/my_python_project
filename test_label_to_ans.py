import csv
import os

ans_dic={}

with open('test_labels.csv', newline='') as csvfile:
        
    rows = csv.DictReader(csvfile)
    for row in rows:
        name=row["filename"]
        classes=row["class"]
        if name in ans_dic.keys():                       
            if classes in ans_dic[name]:
                temp=ans_dic[name][classes]+1
                ans_dic[name][classes]=temp
            else:
                ans_dic[name][classes]=1                                                        
        else:                                
            ans_dic[name]={classes:1}
   


with open('Allans.csv', 'w', newline='') as csvfile:    
    fieldnames = ["檔名","類別","偵測數量" ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for dic_keys in ans_dic.keys():
        for classs in ans_dic[dic_keys].keys():
            writer.writerow({"檔名":dic_keys,"類別":classs,"偵測數量":ans_dic[dic_keys][classs]})