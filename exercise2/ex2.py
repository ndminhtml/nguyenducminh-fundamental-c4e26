from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

raw_data = conn.read()
content = raw_data.decode("utf8")

with open("cafef.html", "wb") as f:
    f.write(raw_data)

#Find ROI
#soup = BeautifulSoup(content, "html.parser")
