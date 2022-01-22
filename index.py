# coding:utf-8
max=50
import json
import random
import requests
import time
import csv
import os

requests.encoding = 'utf-8'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
userlists = []
fs = dict({})


os.system('del test.csv')
def getData(uid, page):
    res = requests.get('https://api.bilibili.com/x/relation/followings?vmid=%d&pn=%d' % (uid, page), headers=headers)
    return json.loads(res.text)


def knowTotalData(uid):
    i = 1
    while True:
        print(uid,i)
        a = getData(uid, i)
        i += 1
        time.sleep(0.5)
        # print(a)
        if a['code'] == 0:
            if not a['data']['list']:
                break
            else:
                knowData(a)
        else:
            break


def knowData(a):
    b = a['data']['list']
    for i in b:
        if i["uname"] in fs:
            fs[i["uname"]] += 1
        else:
            fs[i["uname"]] = 1


i = 1
while i <= max:
    a = random.randint(1, 900000000)
    userlists.append(a)
    i += 1
print(userlists)
for i in userlists:
    knowTotalData(i)
# print(fs)

fs_order=sorted(fs.items(),key=lambda x:x[1],reverse=True)
# print(fs_order)

with open("test.csv",'a+',encoding='gbk') as f:
    for i in fs_order:
        write=csv.writer(f)
        write.writerow(i)
    print("写入完毕！")