#TODO:已完成下载，下一步为解压压缩包，并将插件目录复制到新文件夹，再删除此文件夹。删除可以先调起新的目录的文件，再反过来删除此文件夹。

import requests
from os import getcwd
response = requests.get("https://api.github.com/repos/zhongyang219/TrafficMonitor/releases/latest")
rr = response.json()["tag_name"]
rf = float(rr.replace('V', ''))
with open('v.txt', 'r') as f:
    r = f.read()
    if float(r.replace('V', '')) < rf:
        aask = input('检测到更新，是否更新？(y/n)\nupdater>')
        if aask == 'y':
            r1 = response.json()["assets"][0]["id"]
            response1 = requests.get('https://api.github.com/repos/zhongyang219/TrafficMonitor/releases/assets/'+str(r1))
            rn = response1.json()["name"]
            rrul = response1.json()['browser_download_url']
            p = getcwd().replace('AKDWPythonCMD\core', '')
            r = requests.get(rrul)
            np = p+'/'+rn
            with open(np, "wb") as f:
                f.write(r.content)
        else:
            print('OK')
#print(response.json()["tag_name"])