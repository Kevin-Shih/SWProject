from __future__ import unicode_literals
import bs4
import time
import json
from selenium import webdriver
from urllib.request import urlopen

#browser = webdriver.Chrome(executable_path='C:\Code\VirusCrawler\venv\Lib\site-packages\selenium\webdriver\remote\chromedriver.exe')
def crawler():
    option = webdriver.ChromeOptions()									#設定selenium browser 為chorme
    option.headless = True										#設定不顯示視窗
#    browser = webdriver.Chrome(executable_path='C:\Code\VirusCrawler\venv\Lib\site-packages\selenium\webdriver\remote\chromedriver.exe')
    browser = webdriver.Chrome(executable_path='C:\Code\VirusCrawler\venv\Lib\site-packages\selenium\webdriver\remote\chromedriver.exe',options=option)
    url = "https://www.taoyuan-airport.com/main_ch/revised_flight.aspx?uid=159&pid=12"			#桃機網站url
    browser.get(url)
    time.sleep(3)											#等待網頁加載完成
    html_source = browser.page_source									#抓取加載完的網頁原始碼
    browser.quit()
    root = bs4.BeautifulSoup(html_source, "html5lib")
    flights = root.find("tbody", class_="tt_body").findAll("tr")					#找到存有資訊的表格再find所有航班(每個tr)
    flight_info = []
    for flight in flights:										#對每個航班都執行
        raw_flight_table_infos = flight.findAll("td", class_="flight-table-info")
        temp = ""
        if raw_flight_table_infos:									#如果有抓到航班資訊
            airline_logos = raw_flight_table_infos[2].findAll("img")					#找logo的標籤
            airline_names = raw_flight_table_infos[2].findAll("span")					#找航空公司名稱
            flight_numbers = raw_flight_table_infos[3].findAll("span")					#找航班編號
            temp += raw_flight_table_infos[0].get_text() + "," + raw_flight_table_infos[1].get_text() + "," #拼成字串(每個欄位用','分隔，超過一個航班編號時以' '分隔)
            for airline_logo in airline_logos:
                temp += "https://www.taoyuan-airport.com" + airline_logo['src'] + " "
            temp = temp.rstrip()
            temp += ","
            for airline_name in airline_names:
                temp += airline_name.get_text() + " "
            temp = temp.rstrip()
            temp += ","
            for flight_number in flight_numbers:
                temp += flight_number.get_text() + " "
            temp = temp.rstrip()
            temp += ","
            temp += raw_flight_table_infos[4].get_text() + "," \
                + raw_flight_table_infos[8].get_text() + ","
            flight_info.append(temp)									#將此一航班資訊append進去陣列
    return flight_info											# 回傳所有航班資訊


flight_info_json = json.dumps(crawler(), ensure_ascii=False, separators=('\n', ': '))			#將分隔航班的符號改為'\n'
print(flight_info_json)