from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from time import sleep
from random import random

# binary file needed for using browser
DRIVER_PATH = './driver/chromedriver'


# allows headless option where a Chrome window won't have to open
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

# a temporary list of names/IDs
templist = []
# keep track of the current line for week-to-week uses
current_line = 0
names_list = open('already_used_names.txt').readlines()
# FROM LINE 37
def search_names(templist, current_line):
    # creates webdriver
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get("https://a073-ils-web.nyc.gov/inmatelookup/pages/home/home.jsf")

    for i in range(0, len(names_list)-1):
        current_name = names_list[current_line].strip()
        if current_line < 99:
            current_line +=1
            print('added', current_line, names_list[current_line].strip())
        else:
            current_line = 0
        try:
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
                name = name = driver.find_element_by_xpath(f"/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[{row}]/td[1]").text
                booking_id = driver.find_element_by_xpath(f"/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[{row}]/td[4]").text
                current_facility = driver.find_element_by_xpath(f"/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[{row}]/td[5]").text
                discharge_date = driver.find_element_by_xpath(f"/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[{row}]/td[6]").text
                
                # if not discharged & list is less than 50 add to list
                if not discharge_date:
                    if len(templist) < 2500:
                        person_dict = {
                        'name': name,
                        'booking_id': booking_id,
                        'current_facility': current_facility
                    }
                        templist.append(person_dict)
                    else:
                        # when the list is 50 or above, break
                        break
                else:
                    continue
                # click back to main element
            driver.find_element_by_xpath("//*[@id='home_form:j_id_35']").click()  
        except Exception as e: 
            print(driver.page_source)
            print('error: ', e)
    if len(templist) > 0:
        # temp export of data to CSV for Printing etc 
        data_frame = pd.DataFrame(templist)
        data_frame.to_csv('new_table.csv')
    templist = []
    driver.quit()
    return templist, current_line

search_names(templist, current_line)
