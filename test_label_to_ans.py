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
        
print(ans_dic)

