import requests
import re
from urllib.request import Request, urlopen
import wget
# num_of_pics = input("Enter a number of doggies you want to download:\n")
num_of_pics = int(input("Enter a number of doggies u want to download:\n"))
url = "http://shibe.online/api/shibes?count=%d&urls=%s&httpsUrls=false"
pic_urls = requests.get(url=url % (num_of_pics,"true")).json()
names = open("filenames.txt", "w")
for i in pic_urls:
    req = Request(
        i,
        headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    file_name = re.search("/\\w+.jpg", i).group()[1:]
    fhand = open("Images/"+file_name, 'wb')
    fhand.write(webpage)
    fhand.close()
    names.write(file_name.replace(".jpg", "\n"))


