import requests
from time import gmtime, strftime
from csv import writer
from bs4 import BeautifulSoup
import re

URL = "https://www.lttstore.com/products/backpack"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

#Web scraping LTT backpack stock and wave
#stock = soup.find('span', attrs={'id':'backpack-stock'}).text
#remaining = soup.find(id="backpack-remaining")

in_stock_helper = soup.find(id="back-in-stock-helper").get_text()

#quantity = in_stock_helper[-13:-8]

extract_numbers = re.findall(r'\d+', in_stock_helper)

quantity = extract_numbers[-1]

datetime = strftime("%Y-%m-%d %H:%M:%S")

data = [quantity,datetime,in_stock_helper]
print(data)

with open('ltt_data.csv', 'a+', newline='') as write_obj:
    csv_writer = writer(write_obj)
    csv_writer.writerow(data)

#value = re.findall(r'_BISConfig.product.variants', soup)
#print(value)

URL = "https://www.lttstore.com/products/screwdriver"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

in_stock_helper = soup.find(id="back-in-stock-helper").get_text()

extract_numbers = re.findall(r'\d+', in_stock_helper)

quantity_1 = extract_numbers[-7]
quantity_2 = extract_numbers[-5]
quantity_3 = extract_numbers[-3]
quantity_4 = extract_numbers[-1]

datetime = strftime("%Y-%m-%d %H:%M:%S")

data = [quantity_1,quantity_2,quantity_3,quantity_4,datetime,in_stock_helper]
print(data)

with open('ltt_data_screwdriver.csv', 'a+', newline='') as write_obj:
    csv_writer = writer(write_obj)
    csv_writer.writerow(data)