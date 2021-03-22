# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 09:07:08 2019

@author: Elaine
"""

f1 = open('C:/Users/Elaine/Desktop/Python/file15.txt',encoding='utf8')
s = f1.read()
f1.close()

#把每欄拆開
s1 = s.replace('\\','')
s2 = s1.split('\t')

#第三欄、第四欄未分開
#for i in range(1,len(s2)):
#    if i%3==0:
#        print(s2[i])

for i in range(1,len(s2)):
    if i%3==0:                                      #把第三欄&第四欄   拆開
        s2[i] = s2[i].split('\n')                   



#四個欄位四個list
        
#1.內文
ls_ct = []
for i in range(1,len(s2)):
    if i%3==1:
        ls_ct.append(s2[i])

#2.正評分數
ls_ps = []
for i in range(1,len(s2)):
    if i%3==2:
        ls_ps.append(s2[i])

#3.負評分數
ls_ng = []
for i in range(1,len(s2)):
    if i%3==0:
        ls_ng.append(s2[i][0])
                        
#4.標題
ls_ti = []
for i in range(1,len(s2)):
    if i%3==0:
        ls_ti.append(s2[i][1])
        
#這些資料組成二維list
ls_total = [ls_ti,ls_ct,ls_ps,ls_ng]


#ptt 2017年 食物版
#輸入關鍵字 → (1) 標題+內文共幾個  (2)有幾個"好吃"  (2) 這些文章的網路聲量總分 (正聲量-負聲量)   
        

n = input()
#標題一共幾個
qt_title = str(ls_total[0]).count(n)
#內文一共幾個
qt_content = str(ls_total[1]).count(n)

#輸入關鍵字→ 出現幾個好吃?
good_food = 0
for i in range(1,len(ls_total[1])):
    if ls_total[1][i].find(n) !=-1:
        good_food += ls_total[1][i].count('好吃')
#輸入關鍵字→ 出現幾個讚?
great = 0
for i in range(1,len(ls_total[1])):
    if ls_total[1][i].find(n) !=-1:
        great += ls_total[1][i].count('讚')

#輸入關鍵字→ 得到總分?
point = 0
for i in range(1,len(ls_total[1])):
    if ls_total[1][i].find(n) !=-1:
        point += (eval(ls_total[2][i])-eval(ls_total[3][i]))
    

print(n,'總共在ptt食物版出現了:',qt_title+qt_content,'次~')
print(n,'一共得到了',good_food,'個「好吃」')
print(n,'一共得到了',great,'個「讚」')
print(n,'在ptt食物版中，文章聲量是','%.2f'%(abs(point)),'分')





