from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
import re
import time

n = int(input("Enter the number of photo: "))
html = urlopen(input("Enter the URL: "))

bsObj = BeautifulSoup(html.read(), "html.parser")
images = bsObj.findAll("img", {"src": re.compile("view")})

for image in images:
    print(image["src"].replace("m", "large").replace("ilargeg3.doubanio.colarge", "img3.doubanio.com").replace(
        "ilargeg1.doubanio.colarge", "img1.doubanio.com"))  # 豆瓣图片URL
    n += 1
    imagefilename = "image/" + str(n) + ".jpg"
    url = image["src"].replace("m", "large").replace("ilargeg3.doubanio.colarge", "img3.doubanio.com").replace(
        "ilargeg1.doubanio.colarge", "img1.doubanio.com")
    urllib.request.urlretrieve(url, imagefilename)
    time.sleep(3)

print("Ha!Ha! The Pictures Downloaded!")
time.sleep(5)
print("The number of pictures: ", n)
print("Bye-Bye")
time.sleep(3)
