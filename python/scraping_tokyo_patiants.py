# coding: UTF-8
from bs4 import BeautifulSoup
import requests
import datetime

# issue: datetimeが日本時間じゃない

url_tokyo_municipality = "https://stopcovid19.metro.tokyo.lg.jp/cards/number-of-confirmed-cases-by-municipalities/"
dir_name = "../data/"
today = datetime.date.today().strftime("%Y_%m_%d")
csv_header = ["Date", "Area", "Furigana", "Municipality", "Num_cases"]

def main():
    html_soup = open_url(url_tokyo_municipality)
    tokyo_list = scrape_municipality(html_soup) # [日付, 区分け, なまえ, 名前, 感染者数]
    save_csv(tokyo_list, "tokyo_" + today)

def open_url(url):
    "BeautifulSoupでurl先を解析"
    html = requests.get(url)
    html.encoding = html.apparent_encoding
    return BeautifulSoup(html.text, "html.parser")

def scrape_municipality(soup):
    "公式サイトで[区分け, なまえ, 名前, 感染者数] データを取り、[日付, 区分け, なまえ, 名前, 感染者数] で返す"
    tr_class_include_all_items = soup.select("#app > div > div > main > div > div > div > div > div > div.DataView-CardText > div > div > table > tbody > tr")
    # print(type(tr_class_include_all_items)) # <class 'bs4.element.ResultSet'> # 各タグ部分の1次元リスト #参考 https://qiita.com/Senple/items/c8faf02a944945529f6b
    # print(type(tr_class_include_all_items[0])) # <class 'bs4.element.Tag'> # タグ部分のコード
    data_string = [[data.string for data in items.find_all("td")] for items in tr_class_include_all_items] # 各タグ内の文字列を2次元リストで返す
    for data_string_row in range(len(data_string)):
        data_string[data_string_row].insert(0, datetime.date.today().strftime("%Y_%m_%d")) 
    return data_string
    

def save_csv(data_list, prefecture):
    ""
    import csv
    with open(dir_name + prefecture + ".csv", "w") as municipality_datas:
        writer = csv.writer(municipality_datas, lineterminator = "\n")
        writer.writerow(csv_header)
        writer.writerows(data_list)

if __name__ == "__main__":
    main()