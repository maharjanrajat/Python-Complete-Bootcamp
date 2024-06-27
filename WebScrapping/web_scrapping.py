from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json


options = webdriver.ChromeOptions()
options.add_argument('--headless')


browser = webdriver.Chrome()
browser.get("https://www.sharesansar.com/existing-issues")
time.sleep(3)
table_el= browser.find_element(By.ID,'myTableEip')
time.sleep(1)

table_rows_el = table_el.find_elements(By.TAG_NAME,'tr')

table_data = []

for row in table_rows_el[1:]:
    table_data_el = row.find_elements(By.TAG_NAME, 'td')
    
    ipo = {
        'S.N': table_data_el[0].text,
        'Symbol': table_data_el[1].text,
        'Company': table_data_el[2].text,
        'Units': table_data_el[3].text
    }
    table_data.append(ipo)

with open('ipo_data.json', 'w') as f:
    json.dump(table_data, f, indent=2)
    
browser.close()
