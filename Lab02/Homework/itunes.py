import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from youtube_dl import YoutubeDL

url = 'https://www.apple.com/itunes/charts/songs/'

html_content = urlopen(url).read().decode('utf-8')

soup = BeautifulSoup(html_content, "html.parser")

ul = soup.find("section", "section chart-grid") # CLASS ATTRIBUTE!!!

songs = []

li_list = ul.find_all("li") 
for li in li_list:
    h3 = li.h3 
    h4 = li.h4
 
    dic = {
        "Songs": h3.string,
        "Artists": h4.string
    }
    songs.append(dic)

pyexcel.save_as(records = songs, dest_file_name = "itunesTopsongs.xlsx")

#download
# options = {
#     'default_search': 'ytsearch',
#     'max_download': 1
# }
# s = dic['Songs']
# a = dic['Artists']
# YoutubeDL(options).download(['s'+'a'])