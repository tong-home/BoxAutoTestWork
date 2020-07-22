#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/10 16:45
# @Author : Carpe diem
# @File : test.py


import websocket
import json
import time
url = 'wss://jwai-test.brandwisdom.cn'
#ws = websocket.create_connection(url)
t =  time.time()
id = int(round(t * 1000000))
content = "播放DVD"
contents = content.split("|")
print(len(contents))
i = 0
while i < len(contents):
    ws = websocket.create_connection(url)
    data = {"action":1,"aiNumber":"301001","sessionId":id,"speakerId":"ZHAIGJ1HTD0000002","supportFuncs":[],"text":contents[i],"type":0}
    ws.send(json.dumps(data))
    res = ws.recv()
    print(contents[i]+"\n"+json.loads(res)['text'])
    print("-------------------------")
    i = i+1
    ws.close()


def bubble_sort(alist):
    for j in range(len(alist)-1,0,-1):
    ## j是从第一个数到最后一个数需要移动的次数
        for i in range(j):
            if alist[i]<alist[i+1]:
                #alist[i],alist[i+1]=alist[i+1],alist[i]
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                print(alist)
    return alist
li=[54,26,93,17,77,31,44,55,20]
bubble_sort(li)
print(li)
print(len(li))
