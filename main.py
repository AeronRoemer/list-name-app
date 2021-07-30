from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import json
from time import sleep
from random import random

# binary file needed for using browser
DRIVER_PATH = './driver/chromedriver'

# allows headless option where a Chrome window won't have to open
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

# with open guarantees file closing after use, may prevent errors.
# keep track of the current line for week-to-week uses
with open("nyc-current-script-data.txt") as j:
    data = json.load(j)

with open('top_100.txt') as f:
    names_list = f.readlines()

def search_names(data):
    templist = []
    # creates webdriver
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get("https://a073-ils-web.nyc.gov/inmatelookup/pages/home/home.jsf")

    while len(templist) < 50:
        current_line = data['current_line']
        current_name = names_list[current_line].strip()
        try:
            print('finding')
            # wait until current name form is present to add name and submit via click
            sleep(15+(random()*30))
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='home_form:search_btn']")))
            # adds current name to last name search form area and submits search, driver holds results
            driver.find_element_by_xpath("//*[@id='home_form:j_id_25']").send_keys(current_name)
            driver.find_element_by_xpath("//*[@id='home_form:search_btn']").click()
            # gets rows and cols of table returned from search
            # 1 added to length to account for header, looks at all rows: /tbody/tr
            rows = 1 +len(driver.find_elements_by_xpath("/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr"))
            # looks at all cols in a given row: /tr[1]/
            for row in range(1, rows):
                name = driver.find_element_by_xpath(f"/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[{row}]/td[1]").text
                booking_id = driver.find_element_by_xpath(f"/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[{row}]/td[4]").text
                current_facility = driver.find_element_by_xpath(f"/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[{row}]/td[5]").text
                discharge_date = driver.find_element_by_xpath(f"/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[{row}]/td[6]").text
                
                # if not discharged & list is less than 50 add to list
                if len(templist) < 50:
                    if not discharge_date:
                        person_dict = {
                        'name': name,
                        'booking_id': booking_id,
                        'current_facility': current_facility
                    }
                        templist.append(person_dict)
                    else:
                        # when the list is 50 or above, break
                        print('continued')
                        continue
                else:
                    # exit condition for when the list is over 50 partway through a name
                    # if the list has data, return it. 
                    if len(templist) > 0:
                        print('final condition')
                        # temp export of data to CSV for Printing etc 
                        data_frame = pd.DataFrame(templist)
                        data_frame.to_csv('new_table.csv')
                        
                    else:
                        print('No Names Returned, an error occured')
                    return True
                # click back to main element
            driver.find_element_by_xpath("//*[@id='home_form:j_id_35']").click()  
        except Exception as e: 
            print(driver.page_source)
            print('error: ', e)

        # increment name index if the loop finishes with 50 or less names
        print('runs each loop')
        if current_line < 99:
            current_line +=1
            print('added', current_line, names_list[current_line].strip())
        else:
            current_line = 0
        
    with open("nyc-current-script-data.txt", "w") as json_file:
        data['current_line'] = current_line
        json.dump(data, json_file)
    driver.quit()
    return True

search_names(data)
print(data)