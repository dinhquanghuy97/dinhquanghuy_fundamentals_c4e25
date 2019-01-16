from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode("utf8")

soup = BeautifulSoup(content, "html.parser")
table = soup.find("table", id= "tableContent")

tr_list = table.find_all("tr")
report = []
for tr in tr_list:
    td_list = tr.find_all("td", "b_r_c")
    for td in td_list:
        td = td.string
        vnm = OrderedDict({
            "": td
        })
        report.append(vnm)

pyexcel.save_as(records=report, dest_file_name="VNM report.xlsx")
