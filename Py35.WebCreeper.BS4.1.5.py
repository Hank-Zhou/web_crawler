from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
import re
import time

file = open('image/number', 'r')
n = int(file.read())
html = urlopen(input("Enter the URL: "))

bsObj = BeautifulSoup(html.read(),"html.parser")
images = bsObj.findAll("img", {"src": re.compile(".jpg")})

for image in images:
    print(image["src"].replace("/50/","/").replace("_hd","_r"))
    n += 1
    imagefilename = "image/" + str(n) + ".jpg"
    url = image["src"].replace("/50/","/").replace("_hd","_r")
    urllib.request.urlretrieve(url,imagefilename)
    time.sleep(5)

file.close()
print("Ha!Ha! The Pictures Downloaded!")
file2 = open('image/number', 'w+')
file2.write(str(n))
file2.close()
print("Bye-Bye")
time.sleep(3)
