from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request
import re
import time

file1 = open('image/number', 'r')
n = int(file1.read())
file1.close()
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
file2 = open('image/number', 'w+')
file2.write(str(n))
file2.close()
time.sleep(5)
print("The number of pictures: ", n)
print("Bye-Bye")
time.sleep(3)
