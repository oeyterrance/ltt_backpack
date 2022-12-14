import requests
from time import gmtime, strftime
from csv import writer
from bs4 import BeautifulSoup
import re

#########################################################################################################
#LTT Backpack Code below
#########################################################################################################

datetime = strftime("%Y-%m-%d %H:%M:%S")

# URL = "https://www.lttstore.com/products/backpack"

# page = requests.get(URL)
# soup = BeautifulSoup(page.content, "lxml")

# quantity = re.search(r'\d+', re.search(r'inventoryQuantity\s*=\s*\d+', str(soup)).group(0))

# data = [quantity.group(0),datetime]

# with open('ltt_data.csv', 'a+', newline='') as write_obj:
#     csv_writer = writer(write_obj)
#     csv_writer.writerow(data)


#########################################################################################################
#LTT Screwdriver Code below
#########################################################################################################

URL = "https://www.lttstore.com/products/screwdriver"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "lxml")

quantity1 = re.search(r'\d+', re.search(r'inventoryQuantity\s*=\s*\d+', str(soup)).group(0))

data1 = [0,0,0,0,datetime,quantity1.group(0)]

with open('ltt_data_screwdriver.csv', 'a+', newline='') as write_obj:
    csv_writer = writer(write_obj)
    csv_writer.writerow(data1)

print("Current Date-Time: ", datetime)
# print("LTT Backpack Quantity:", quantity.group(0))
print("LTT Screwdriver Quantity:", quantity1.group(0))



