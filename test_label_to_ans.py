import csv
import os

ans_dic={}

with open('test_labels.csv', newline='') as csvfile:
        
    rows = csv.DictReader(csvfile)
    for row in rows:
        name=row["filename"]        
        if name in ans_dic.keys():
            ans_dic[name]=ans_dic[name]+1
        else:            
            ans_dic[name]=1
print(ans_dic)
'''
 with open('test_label_ans.csv', 'w', newline='') as csvfile:
        fieldnames = ['filename', "偵測數量" ]
'''