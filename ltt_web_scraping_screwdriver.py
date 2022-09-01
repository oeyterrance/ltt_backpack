import requests
from time import gmtime, strftime
from csv import writer
from bs4 import BeautifulSoup
import re

URL = "https://www.lttstore.com/products/screwdriver"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

in_stock_helper = soup.find(id="back-in-stock-helper").get_text()

extract_numbers = re.findall(r'\d+', in_stock_helper)

#quantity_1 = in_stock_helper[-218:-213]
#quantity_2 = in_stock_helper[-149:-144]
#quantity_3 = in_stock_helper[-80:-76]
#quantity_4 = in_stock_helper[-12:-8]

quantity_1 = extract_numbers[-7]
quantity_2 = extract_numbers[-5]
quantity_3 = extract_numbers[-3]
quantity_4 = extract_numbers[-1]

#print(quantity_1)
#print(quantity_2)
#print(quantity_3)
#print(quantity_4)

datetime = strftime("%Y-%m-%d %H:%M:%S")

data = [quantity_1,quantity_2,quantity_3,quantity_4,datetime,in_stock_helper]

with open('ltt_data_screwdriver.csv', 'a+', newline='') as write_obj:
    csv_writer = writer(write_obj)
    csv_writer.writerow(data)
