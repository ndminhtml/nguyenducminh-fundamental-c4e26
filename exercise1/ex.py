#Part 1
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL
#1. Creat connection
url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)

#2. Dowload page

raw_data = conn.read()
content = raw_data.decode("utf8")


# f = open("itunes.html", "wb")
# f.write(raw_data)
# f.close

#3. Find ROI

soup = BeautifulSoup(content, "html.parser")

ul_tops = soup.find("ul", "")
#print(ul_tops)

#4. Copy n Save
li_list = ul_tops.find_all("li")
new_list=[]
for li in li_list:
    h3 = li.h3
    a  = h3.a 
    songs = a.string
    h4 = li.h4
    a = h4.a
    artist = a.string
    tops = {
        "songs" : songs,
        "artist": artist
    }
    print(tops)
    new_list.append(tops)

#5. Save

pyexcel.save_as(records= new_list , dest_file_name="ex.xlsx")

#Part 2
options = {
    "default_search": "ytsearch",
    "max_downloads" : 100,
    "format" : "bestaudio/audio"
}
dl = YoutubeDL(options)
for i in new_list:
    print(i)
    dl.download(["i"])