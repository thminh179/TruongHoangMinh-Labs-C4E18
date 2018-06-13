#1. download webpage: use: urllib
import urllib
from urllib.request import urlopen 
from bs4 import BeautifulSoup
import pyexcel

url = "http://dantri.com.vn/"

#1.1. Create a connection
connect = urlopen(url)

#1.2. Read
data = connect.read() 

#1.3. Decode
html_content = data.decode("utf-8") 

#short version: combine 1.1 1.2 1.3
    # html_content = urlopen(url).read().decode('utf-8')

# print(html_content)

#1.4. Save website to file
# urllib.request.urlretrieve(url, "dantri.html")
# f = open("dantri2.html", "wb") #add 'b' to open file in binary mode  
# f.write(html_content)
# f.close()

#2. Extract ROI (Region of Interest) 
soup = BeautifulSoup(html_content, "html.parser")

# print (soup.prettify()) 

ul = soup.find("ul", "ul1 ulnew") #find(name, attribute(*mặc định là kiểu class))
# print(ul.prettify())

article_lists = [] #khai báo list các bài báo cần xuất

li_list = ul.find_all("li")
for li in li_list:
    # print(li.prettify())
    # print("* "*20)
    h4 = li.h4 #~find h4 in li
    a = h4.a #~ find a in h4 -> shortening: a = li.h4.a
    # print(a.string) #lấy ra string của thẻ
    print(a['href']) #lấy ra đường dẫn của thẻ
    print(url + a['href']) #lấy ra url đầy đủ
    dic = { # khai báo dict trong article_list
        "Title": a.string,
        "Link" : url + a['href']
    }
    article_lists.append(dic) #đẩy dic vào list

#3. Extract data (info) 

# print (article_lists) 
pyexcel.save_as(records = article_lists, dest_file_name = "dantri.xlsx")