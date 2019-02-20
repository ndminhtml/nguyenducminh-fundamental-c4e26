from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel 
#1. Creat connection
url = "https://dantri.com.vn"
conn = urlopen(url)

#2. Dowload page
raw_data = conn.read()
page_content = raw_data.decode("utf8")

with open("dantri.html", "wb") as f:
    f.write(raw_data)


#3. Find ROI
# soup = BeautifulSoup(page_content, "html.parser")
# ul = soup.find("ul", "ul1 ulnew")

#4. Extract ROI

# li_list = ul.find_all('li')
# news_list = []
# for li in li_list:
#     h4 = li.h4
#     a = h4.a
#     link = url + a["href"]
#     title = a.string
#     news = {
#         "link": link,
#         "title": title,
#     }
#     news_list.append(news)



#5. Save

#pyexcel.save_as(records= news_list, dest_file_name="cranl_data_intro.xlsx")