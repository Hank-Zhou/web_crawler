from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
import re
import time

file = open('D:\\Scrap Photo\\number', 'r')         # 2018/4/21 19:19
n = int(file.read())                                # 2018/4/21 19:19
html = urlopen(input("Enter the URL: "))

bsObj = BeautifulSoup(html.read(),"html.parser")
images = bsObj.findAll("img", {"src": re.compile(".jpg")})

for image in images:
    print(image["src"].replace("/50/","/").replace("_hd","_r"))
    n += 1
    imagefilename = "D:\\Scrap Photo\\" + str(n) + ".jpg"
    url = image["src"].replace("/50/","/").replace("_hd","_r")
    urllib.request.urlretrieve(url,imagefilename)
    time.sleep(5)

file.close()
print("Ha!Ha! The Pictures Downloaded!")
file2 = open('D:\\Scrap Photo\\number', 'w+')       # 2018/4/21 19:19
file2.write(str(n))
file2.close()
print("Bye-Bye")
time.sleep(3)
