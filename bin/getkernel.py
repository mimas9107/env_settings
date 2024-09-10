#!/usr/bin/env python
import os
import sys
import requests
from bs4 import BeautifulSoup 

# Linux kernels have version numbers in the format x.y.z. 
# x is the major release number, y is the minor revision number, and z is the patch number. 
# PLEASE NOTE: z is NOT the number of patches; 
# it simply indicates that more bugs have been fixed since the last patch number.
def parseversion(text):
    text = str(text)
    text = text.strip(" ")
    if(text.count("-")):
        [ver,desc] = text.split("-")
    else:
         ver = text
    if( "." in ver):
        return ver.split(".")        
    else:
        return [-1,-1,-1];

res = os.popen("uname -r").readline()
print("\t 目前 kernel版本：\t",res)
myversion = parseversion(res)
# print(myversion)

url = "https://kernel.org"
# f=open("kernel.html","r")
# results = f.read()
# f.close

results = requests.get(url)

soup = BeautifulSoup(results.text,"lxml")


print("===== kernel.org =====")
#print(soup.select("table")[2].select("tr"))
for ele in soup.select("table")[2].select("tr"):
    tmp = parseversion(ele.select("td")[1].text)
    
    if(int(tmp[0])!=int(myversion[0])):
        pass
    else:
        if(int(tmp[1])==int(myversion[1])):
            print("\t kernel.org官網版本：\t",ele.select("td")[1].text)
            print("\t ",ele.select("td")[2].text)
            print("\t ",ele.select("td")[3].select("a")[0]['href'])
            newer_kernel_link=ele.select("td")[3].select("a")[0]['href']
            break          

if(int(myversion[2]) <= int(tmp[2])):
    print("\t 有比較新的 kernel版本！\t ")

    newer_kernel_file = newer_kernel_link.strip("https://").split("/")[-1]
    if(os.path.exists(newer_kernel_file)):
        print("\t 已有新版 kernel檔案包存在！ \t")
    else:
        YN = input("\t 你要下載嗎? Y/n") 
        if(YN == '' or YN == 'y' or YN == 'Y'):
            res = os.system("wget {}".format(newer_kernel_link))
            print("\t 完成！") 
        
        else:
            pass       
    # for td in ele.select("td"):
    #     print(td.text)

