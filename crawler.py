import requests
import os
from pathlib import Path
from bs4 import BeautifulSoup


def trace_spider(max_pages):
    my_file = Path("/home/patrick/.PyCharmCE2018.3/config/scratches/autovit.txt")
    if my_file.is_file():
        os.remove(my_file)
    fw = open('autovit.txt', 'w')
    page = 1
    while page <= max_pages:
        url = "https://www.autovit.ro/autoturisme/audi/?search%5Bfilter_float_price%3Ato%5D=65000&search%5Border%5D=filter_float_price%3Adesc&search%5Bcountry%5D=&page=" + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {"class":"offer-title__link"}):
            href = link.get("href")
            # print(href)
            # get_single_item_data2(href)
            get_single_item_data(href, fw)
            fw.write("\n" + "\n" + "\n")
        page += 1
    fw.close()

def get_single_item_data(item_url, fw):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    vect1 = []
    vect2 = []
    for item_name in soup.findAll('span', {"class":"offer-params__label"}):
        vect1.append(item_name.string)

    for item_name in soup.findAll('a', {"class":"offer-params__link"}):
        vect2.append(item_name.string)

    for (a, b) in zip(vect1, vect2):
        c = str(a) + "    " + str(b)
        fw.write(c + "\n")
    del vect1[:]
    del vect2[:]



def get_single_item_data2(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.findAll('span', {"class":"offer-params__label"}):
        print(item_name.string)
trace_spider(1)