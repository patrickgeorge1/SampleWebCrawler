import modules
import random
from urllib import request   ## import urllib.request

def download_web_image(url):                  # Image downloader
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)          //urlretrieve(url, name)

# download_web_image("https://i.pinimg.com/564x/d6/8b/2e/d68b2edc0225ee096bcdec949bcdac93.jpg")

'''
fw = open('sample.txt', 'w')                       RW files
fw.write('Writing some stuff in my text file\n')
fw.write('I like bacon\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
fr.close()
print(text)
'''




goog_url = 'https://sample-videos.com/csv/Sample-Spreadsheet-1000-rows.csv' # descarcare csv

'''def download_stock_data(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, 'w')
    for line in lines:
        fx.write(line + '\n')
    fx.close();

download_stock_data(goog_url)
'''


