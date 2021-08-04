from logging import error
from django.shortcuts import get_list_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout

from .models import NYCAlready, NYCCurrent


## SELENIUM STUFF
# ----------------------
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
with open("./namesapp/nyc-data/nyc-current-script-data.txt") as j:
    data = json.load(j)

with open('./namesapp/nyc-data/top_100.txt') as f:
    names_list = f.readlines()


def check_and_add_name(person, templist):
    if NYCAlready.objects.filter(pk=person['book_and_case']).exists():
        print('found', person)
    else:
        new_person = NYCAlready(pk=person['book_and_case'], name=person['name'], location=person['location'])
        new_person.save()
        templist.append(person)
        print('saved')
    return templist
    

def search_names(data, input_number=50):
    number = int(input_number)
    templist = []
    current_line = data['current_line']
    # creates webdriver
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
    driver.get("https://a073-ils-web.nyc.gov/inmatelookup/pages/home/home.jsf")

    while len(templist) < number:
        current_name = names_list[current_line].strip()
        try:
            print('finding', current_name)
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
                book_and_case = driver.find_element_by_xpath(f"/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[{row}]/td[4]").text
                location = driver.find_element_by_xpath(f"/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[{row}]/td[5]").text
                discharge_date = driver.find_element_by_xpath(f"/html/body/div[1]/div/div/form/div[3]/div/table/tbody/tr[{row}]/td[6]").text
                
                # if not discharged & list is less than 50 add to list
                if len(templist) < number:
                    if not discharge_date:
                        person_dict = {
                        'name': name,
                        'book_and_case': int(book_and_case),
                        'location': location
                    }
                        # checks to see if person exists, if so adds to list and DB
                        templist = check_and_add_name(person_dict, templist)
                        print(person_dict)
                    else:
                        # skip if there's a discharge date
                        print('continued')
                        continue
                elif len(templist) >= 50:
                    # exit condition for when the list is over 50 partway through a name
                    # if the list has data, return it. 
                    
                    # temp export of data to CSV for Printing etc 
                    data_frame = pd.DataFrame(templist)
                    data_frame.to_csv('./namesapp/nyc-data/new_table.csv')
                    
            # click back to main element
            try:
                item = driver.find_element_by_xpath("//*[@id='home_form:j_id_35']")
                if item.is_displayed() :
                    print('displayed')
                    driver.find_element_by_xpath("//*[@id='home_form:j_id_35']").click()
                else: 
                    driver.find_element_by_xpath("//*[@id='home_form:j_id_1z']").click()  
            except Exception as e:
                print(e)

        except Exception as e: 
            #print(driver.page_source)
            print(e)
            return {'error:': e }

        # increment name index if the loop finishes with 50 or less names
        print('runs each loop')
        if current_line < 99:
            current_line +=1
            print('added', current_line, names_list[current_line].strip())
        else:
            current_line = 0
        
    with open("./namesapp/nyc-data/nyc-current-script-data.txt", "w") as json_file:
        data['current_line'] = current_line
        json.dump(data, json_file)
    driver.quit()
    return templist

# ----------------------
# ----------------------
# ----------------------
# ----------------------
# Create your views here.

def index(request):
    current_line = data['current_line']
    current_name = names_list[current_line].strip()
    context = { 'current_name': current_name, 'current_line': current_line }
    return render(request, 'namesapp/index.html', context)
    
def NYCAllNames(request):
    people = get_list_or_404(NYCAlready)
    context = { 'people': people }
    return render(request, 'namesapp/nyc-all-names.html', context)

def get_names(request):
    number = request.POST['number']
    templist = search_names(data, number)
    context = { 'people': templist, 'number': number }
    return render(request, 'namesapp/submit.html', context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    context = {}
    return render(request, 'namesapp/login.html', context)