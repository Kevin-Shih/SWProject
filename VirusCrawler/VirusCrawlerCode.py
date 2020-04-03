from __future__ import unicode_literals
import bs4
import time
import json
from selenium import webdriver
from urllib.request import urlopen


def crawler():
    option = webdriver.ChromeOptions()
    option.headless = True
    browser = webdriver.Chrome(options=option)
    url = "https://www.taoyuan-airport.com/main_ch/revised_flight.aspx?uid=159&pid=12"
    browser.get(url)
    time.sleep(5)
    html_source = browser.page_source
    browser.quit()
    root = bs4.BeautifulSoup(html_source, "html5lib")
    flights = root.find("tbody", class_="tt_body").findAll("tr")
    flight_info = {

    }
    count = 0
    for flight in flights:
        raw_flight_table_infos = flight.findAll("td", class_="flight-table-info")
        temp = ""
        if raw_flight_table_infos:
            airline_logos = raw_flight_table_infos[2].findAll("img")
            airline_names = raw_flight_table_infos[2].findAll("span")
            flight_numbers = raw_flight_table_infos[3].findAll("span")
            temp += raw_flight_table_infos[0].get_text() + "," \
                + raw_flight_table_infos[1].get_text() + ","
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
                + raw_flight_table_infos[8].get_text()
            flight_info['flight'+str(count)] = temp
            count += 1
            flight_info_json = json.dumps(flight_info, ensure_ascii=False, separators=('\n', ': '))
    return flight_info_json

print(crawler())


