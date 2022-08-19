import requests
from time import gmtime, strftime
from csv import writer
from bs4 import BeautifulSoup

URL = "https://www.lttstore.com/products/backpack"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

#Web scraping LTT backpack stock and wave
#stock = soup.find('span', attrs={'id':'backpack-stock'}).text
#remaining = soup.find(id="backpack-remaining")

in_stock_helper = soup.find(id="back-in-stock-helper").get_text()

quantity = in_stock_helper[-13:-8]
datetime = strftime("%Y-%m-%d %H:%M:%S")

data = [quantity,datetime,in_stock_helper]

with open('ltt_data.csv', 'a+', newline='') as write_obj:
    csv_writer = writer(write_obj)
    csv_writer.writerow(data)





#value = re.findall(r'_BISConfig.product.variants', soup)
#print(value)
