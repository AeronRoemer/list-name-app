from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import pandas as pd
import csv
from time import sleep
from random import random

# binary file needed for using browser
DRIVER_PATH = './driver/chromedriver'

# allows headless option where a Chrome window won't have to open
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

# creates webdriver
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://a073-ils-web.nyc.gov/inmatelookup/pages/home/home.jsf")
templist = []
current_line = 0
names_list = open('top_100.txt').readlines()


def search_names(current_line):
    for r in range(0,1):
        sleep(random()*10)
        current_name = names_list[current_line]
        print(current_name)
        try:
            # keep track of the current line for week-to-week uses
            if current_line < 50:
                current_line =+1
                print('added', current_line)
            else:
                print('reset')
                current_line = 0

            print(driver.page_source)
            # wait until current name form is present to add name and submit via click
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='home_form:search_btn']")))
            # adds current name to last name search form area and submits search, driver holds results
            driver.find_element_by_xpath("//*[@id='home_form:j_id_25']").send_keys(current_name)
            driver.find_element_by_xpath("//*[@id='home_form:search_btn']").click()
            # gets rows and cols of table returned from search
            # 1 added to length to account for header, looks at all rows: /tbody/tr
            rows = 1 +len(driver.find_elements_by_xpath("/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr"))
            # looks at all cols in a given row: /tr[1]/
            # cols = len(driver.find_elements_by_xpath("/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[1]/td"))
            
            for row in range(2, 4):
                name = name = driver.find_element_by_xpath(f"/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[{row}]/td[1]").text
                booking_id = driver.find_element_by_xpath(f"/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[{row}]/td[4]").text
                current_facility = driver.find_element_by_xpath(f"/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[{row}]/td[5]").text
                discharge_date = driver.find_element_by_xpath(f"/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[{row}]/td[6]").text
                # if not discharged & list is less than 50 add to list
                if not discharge_date:
                    if len(templist) < 50:
                        person_dict = {
                        'name': name,
                        'booking_id': booking_id,
                        'current_facility': current_facility
                    }
                        templist.append(person_dict)
                        print(person_dict)
                    else:
                        break
                else:
                    continue
                # click back to main element
                driver.find_element_by_xpath("//*[@id='home_form:j_id_35']").click()  
        except Exception as e: 
            print('error: ', e)
        data_frame = pd.DataFrame(templist)
        data_frame.to_csv('new_table.csv')
        driver.quit()

search_names(current_line)