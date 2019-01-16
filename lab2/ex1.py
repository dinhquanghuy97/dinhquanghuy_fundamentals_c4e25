from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL
url = "https://www.apple.com/itunes/charts/songs"

conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode("utf8")

soup = BeautifulSoup(content, "html.parser")
ul_songs = soup.find("section","section chart-grid")
# print(soup.prettify())
# print(ul_songs)
li_list = ul_songs.find_all("li")
songs_list = []
for li in li_list:
    h3 = li.h3.a
    h4 = li.h4.a
    name = h3.string
    artists = h4.string
    songs = OrderedDict({
        "Song's name": name,
        "Artists": artists,
    })
    songs_list.append(songs)
# print(songs_list)
pyexcel.save_as(records=songs_list, dest_file_name="iTunes top songs.xlsx")
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1 
    }
dl = YoutubeDL(options)

for k in songs_list:
    dl.download(k["Song's name"])