from logging import error
from django.shortcuts import get_list_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import NYCAlready, NYCCurrent
import csv


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
DRIVER_PATH = '/bin/chromedriver'

# allows headless option where a Chrome window won't have to open
options = Options()
options.headless = True
options.add_argument('--no-sandbox')
options.add_argument('--disable-extensions')


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
        NYCCurrent(pk=person['book_and_case'], name=person['name'], location=person['location']).save()
        new_person.save()
        templist.append(person)
        print('saved')
    return templist    

def search_names(data, input_number=50):
    current_line = data['current_line']
    previous_line = data['current_line']
    number = int(input_number)
    templist = []
    # creates webdriver
    print('before driver')
    driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH, service_args=["--verbose", "--log-path=/var/log/namesapp"])
    print('after driver, before get')
    driver.get("https://a073-ils-web.nyc.gov/inmatelookup/pages/home/home.jsf")
    print('after get')
    NYCCurrent.objects.all().delete()
    while len(templist) < number:
        current_name = names_list[current_line].strip()
        try:
            print('finding', current_name)
            # wait until current name form is present to add name and submit via click
            sleep(10+(random()*20))
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
                    print(len(templist))
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
                elif len(templist) >= number:
                    # exit condition for when the list is over 50 partway through a name
                    # if the list has data, return it. 
                    
                    # temp export of data to CSV for Printing etc 
                    data_frame = pd.DataFrame(templist)
                    data_frame.to_csv('./namesapp/nyc-data/new_table.csv')
                    
            # click back to main element
            try:
                item = driver.find_element_by_xpath("//*[@id='home_form:j_id_35']")
                if item.is_displayed():
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
        if current_line < 250:
            current_line +=1
            print('added', current_line, names_list[current_line].strip())
        else:
            current_line = 0
        
    with open("./namesapp/nyc-data/nyc-current-script-data.txt", "w") as json_file:
        print('updated')
        data['current_line'] = current_line
        data['previous_line'] = previous_line
        json.dump(data, json_file)
    driver.quit()
    return templist

def csv_helper(people):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="all-names-list.csv"'},
    )
    writer = csv.writer(response)
    print(people)
    for person in people:
        writer.writerow([person.name, person.book_and_case, person.location])
    return response
# ----------------------
# ----------------------
# ----------------------
# ----------------------
# Create your views here.

@login_required()
def index(request):
    current_line = data['current_line']
    current_name = names_list[current_line].strip()
    context = { 'current_name': current_name, 'current_line': current_line }
    return render(request, 'namesapp/index.html', context)

@login_required   
def NYCAllNames(request):
    people = get_list_or_404(NYCAlready)
    context = { 'people': people }
    print(context)
    return render(request, 'namesapp/ramNYC-all.html', context)

@login_required   
def recent_NYC(request):
    people = get_list_or_404(NYCCurrent)
    current_line = data['current_line']
    previous_line = data['previous_line']
    context = { 'people': people, 'current_line': current_line, 'previous_line': previous_line }
    print(context)
    return render(request, 'namesapp/most-recent-ramNYC.html', context)

@login_required
def get_names(request):
    number = request.POST['number']
    templist = search_names(data, number)
    if request.POST['radio'] and (request.POST['radio'] == '1'):
        csv_helper(templist)
    context = { 'people': templist, 'number': number }
    return render(request, 'namesapp/submit.html', context)

def about(request):
    return render(request, 'namesapp/about.html')

def return_csv_all(request):
    return csv_helper(NYCAlready.objects.all())

def return_csv_recent(request):
    return csv_helper(NYCCurrent.objects.all())

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/namesapp/home')
        else:
            messages.error(request, 'username or password not correct')
            return redirect('./login')

    else:
        form = AuthenticationForm()
    return render(request, 'namesapp/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('/namesapp/home')